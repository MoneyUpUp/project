
from rest_framework.permissions import IsAuthenticated
from .swaggers import products_list_view  # swagger 설정 분리 import
    
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import DepositProduct
from products.serializers import DepositProductSerializer

from .api.fin_api import get_deposit_api

class ProductListView(APIView):
    # get_deposit_api()

    @products_list_view
    def get(self, request):
        products = DepositProduct.objects.all().prefetch_related("options", "bank")
        serializer = DepositProductSerializer(products, many=True)
        return Response(serializer.data)
    
class DepositListView(APIView):
    # get_deposit_api()

    @products_list_view
    def get(self, request):
        products = DepositProduct.objects.all().prefetch_related("options", "bank")
        serializer = DepositProductSerializer(products, many=True)
        return Response(serializer.data)
