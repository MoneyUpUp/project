from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import DepositProduct, SavingProduct
from products.serializers import DepositProductSerializer, SavingProductSerializer
from products.utils.update_checker import should_update, mark_updated
from swaggers.products_swaggers import (
    deposit_list_view,
    saving_list_view,
    all_list_view,
)

from .api.fin_api import get_deposit_api, get_saving_api


class AllListView(APIView):
    @all_list_view
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


class DepositListView(APIView):
    @deposit_list_view
    def get(self, request):
        if should_update("deposit"):
            get_deposit_api()
            mark_updated("deposit")

        products = DepositProduct.objects.all().prefetch_related("options", "bank")
        serializer = DepositProductSerializer(products, many=True)
        return Response(serializer.data)


class SavingListView(APIView):
    @saving_list_view
    def get(self, request):
        if should_update("saving"):
            get_saving_api()
            mark_updated("saving")

        products = SavingProduct.objects.all().prefetch_related("options", "bank")
        serializer = SavingProductSerializer(products, many=True)
        return Response(serializer.data)
