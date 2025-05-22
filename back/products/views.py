from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import DepositProduct, SavingProduct
from products.serializers import DepositProductSerializer, SavingProductSerializer
from products.utils.update_checker import should_update, mark_updated
from swaggers.products_swaggers import deposit_list_view, saving_list_view

from .api.fin_api import get_deposit_api, get_saving_api


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
