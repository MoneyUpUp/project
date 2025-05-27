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

        # DB에서 데이터를 조회합니다.
        prices = SpotAssetPrice.objects.filter(product=spot_asset).order_by("date")

        # 만약 오늘 날짜의 데이터가 없다면, 빈 응답을 반환하거나 적절히 처리합니다.
        # 서버 시작 시 데이터가 채워지므로, 여기서는 추가 API 호출을 하지 않습니다.
        if not prices.exists():
            return Response(
                {"error": f"No historical data found for {commodity_name} in DB."},
                status=status.HTTP_404_NOT_FOUND,
            )

        data = [
            {"date": price.date, "close_price": price.close_price} for price in prices
        ]
        return Response({commodity_name: data})


class ProductListView(APIView):
    authentication_classes = []  # 인증 클래스 비활성화
    permission_classes = [AllowAny]  # 권한 클래스 추가

    @product_list_view
    def get(self, request):
        # DB에서 모든 예금/적금 상품을 조회합니다. (API 호출 로직 제거)
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
