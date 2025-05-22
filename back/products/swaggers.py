from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

products_list_view = swagger_auto_schema(
    operation_summary="예금 적금 모두 불러오기",
    operation_description="예금 적금 상품 리스트를 조회합니다.",
    responses={
        200: openapi.Response(
            description="성공",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'is_authenticated': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    'user': openapi.Schema(type=openapi.TYPE_STRING),
                }
            )
        )
    },
    tags=["Products"]
)