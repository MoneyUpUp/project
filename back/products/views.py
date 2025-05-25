from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import DepositProduct, SavingProduct
from products.serializers import DepositProductSerializer, SavingProductSerializer
from products.utils.update_checker import should_update, mark_updated
from swaggers.products_swaggers import product_list_view


from .api.fin_api import get_deposit_api, get_saving_api


class ProductListView(APIView):
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
