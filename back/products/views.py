from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny  # AllowAny 임포트

from products.models import (
    DepositProduct,
    SavingProduct,
    SpotAssetProduct,
    SpotAssetPrice,
)
from products.serializers import DepositProductSerializer, SavingProductSerializer
from products.utils.update_checker import should_update, mark_updated
from swaggers.products_swaggers import product_list_view, commodity_history_swagger


from .api.fin_api import get_deposit_api, get_saving_api

from .api.yfinance_api import save_asset_prices, TICKER_MAP


class CommodityHistoryView(APIView):
    authentication_classes = []  # 인증 클래스 비활성화
    permission_classes = [AllowAny]  # 권한 클래스 추가

    @commodity_history_swagger
    def get(self, request, commodity_name):
        from django.utils import timezone

        today = timezone.now().date()

        if commodity_name not in TICKER_MAP:
            return Response(
                {"error": "Unsupported commodity."}, status=status.HTTP_400_BAD_REQUEST
            )

        spot_asset, _ = SpotAssetProduct.objects.get_or_create(name=commodity_name)

        spot_price_qs = SpotAssetPrice.objects.filter(product=spot_asset, date=today)
        if not spot_price_qs.exists():
            try:
                save_asset_prices(commodity_name)
            except ValueError as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        prices = SpotAssetPrice.objects.filter(product=spot_asset).order_by("date")
        data = [
            {"date": price.date, "close_price": price.close_price} for price in prices
        ]
        return Response({commodity_name: data})


class ProductListView(APIView):
    authentication_classes = []  # 인증 클래스 비활성화
    permission_classes = [AllowAny]  # 권한 클래스 추가

    @product_list_view
    def get(self, request):
        # 필요한 경우 API에서 최신 데이터를 받아옵니다.
        if should_update("deposit"):
            get_deposit_api()
            mark_updated("deposit")

        if should_update("saving"):
            get_saving_api()
            mark_updated("saving")

        # DB에서 모든 예금/적금 상품을 조회합니다.
        deposits = DepositProduct.objects.all().prefetch_related("options", "bank")
        savings = SavingProduct.objects.all().prefetch_related("options", "bank")

        # 직렬화
        deposit_serializer = DepositProductSerializer(deposits, many=True)
        saving_serializer = SavingProductSerializer(savings, many=True)

        data = {
            "deposit_products": deposit_serializer.data,
            "saving_products": saving_serializer.data,
        }
        # 응답 구조 통일
        return Response(data)
