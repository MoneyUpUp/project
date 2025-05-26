from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

TAG = ["ai"]

recommend_products_swagger = swagger_auto_schema(
    operation_summary="AI 기반 상품 추천 (GET)",
    operation_description="사용자의 투자 성향 및 선호 기간에 따라 AI가 예금 및 적금 상품을 추천하고, 추천 이유를 제공합니다.",
    responses={
        200: openapi.Response(
            description="추천 성공",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "recommendations": openapi.Schema(
                        type=openapi.TYPE_STRING, description="AI가 생성한 추천 이유"
                    ),
                },
            ),
        ),
        401: "인증되지 않은 사용자",
    },
    tags=TAG,
)

chat_bot_swagger = swagger_auto_schema(
    operation_summary="AI 챗봇과 대화 (POST)",
    operation_description="AI 챗봇에게 메시지를 보내고 답변을 받습니다. 챗봇의 응답 스타일을 지정할 수 있습니다.",
    manual_parameters=[
        openapi.Parameter(
            "style",
            openapi.IN_PATH,
            description="챗봇 응답 스타일 (예: default, edgelord)",
            type=openapi.TYPE_STRING,
            required=True,
        ),
    ],
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["message"],
        properties={
            "message": openapi.Schema(
                type=openapi.TYPE_STRING, description="사용자 메시지"
            ),
        },
        example={"message": "안녕, 챗봇!"},
    ),
    responses={
        200: openapi.Response(
            description="답변 성공",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "answer": openapi.Schema(
                        type=openapi.TYPE_STRING, description="챗봇의 답변"
                    ),
                },
            ),
        ),
        400: "잘못된 요청 (메시지 누락)",
    },
    tags=TAG,
)
