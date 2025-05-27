from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from products.serializers import DepositProductSerializer, SavingProductSerializer
from products.serializers import ProductListResponseSerializer

TAG = ["products"]

product_list_view = swagger_auto_schema(
    operation_summary="예금 및 적금 모두 불러오기",
    operation_description="예금과 적금 상품 리스트를 한 번에 조회합니다.",
    responses={200: ProductListResponseSerializer},
    tags=TAG,
)

deposit_list_view = swagger_auto_schema(
    operation_summary="예금 모두 불러오기",
    operation_description="예금 상품 리스트를 조회합니다.",
    responses={200: DepositProductSerializer(many=True)},
    tags=TAG,
)

saving_list_view = swagger_auto_schema(
    operation_summary="적금 모두 불러오기",
    operation_description="적금 상품 리스트를 조회합니다.",
    responses={200: SavingProductSerializer(many=True)},
    tags=TAG,
)

commodity_history_swagger = swagger_auto_schema(
    operation_summary="현물 상품 과거 가격 조회 (GET)",
    operation_description="특정 현물 상품의 과거 가격 데이터를 조회합니다.",
    manual_parameters=[
        openapi.Parameter(
            "commodity_name",
            openapi.IN_PATH,
            description="현물 상품 이름 (예: 'gold', 'oil')",
            type=openapi.TYPE_STRING,
            required=True,
        ),
    ],
    responses={
        200: openapi.Response(
            description="조회 성공",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                additional_properties=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            "date": openapi.Schema(
                                type=openapi.TYPE_STRING, format="date"
                            ),
                            "close_price": openapi.Schema(type=openapi.TYPE_NUMBER),
                        },
                    ),
                ),
            ),
        ),
        400: "지원되지 않는 상품 또는 잘못된 요청",
    },
    tags=TAG,
)
