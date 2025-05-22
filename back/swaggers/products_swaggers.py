from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from products.serializers import DepositProductSerializer, SavingProductSerializer

deposit_list_view = swagger_auto_schema(
    operation_summary="예금 모두 불러오기",
    operation_description="예금 상품 리스트를 조회합니다.",
    responses={200: DepositProductSerializer(many=True)},
    tags=["Products"],
)

saving_list_view = swagger_auto_schema(
    operation_summary="적금 모두 불러오기",
    operation_description="적금 상품 리스트를 조회합니다.",
    responses={200: SavingProductSerializer(many=True)},
    tags=["Products"],
)
