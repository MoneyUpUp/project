from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accounts.serializers import UserSerializer, UserFavoriteProductsSerializer

TAG = ["accounts/me"]

me_get_swagger = swagger_auto_schema(
    operation_summary="유저 정보 조회 (GET)",
    operation_description="현재 로그인한 사용자의 전체 정보를 조회합니다.",
    responses={200: openapi.Response("조회 성공", UserSerializer())},
    tags=TAG,
)

me_patch_swagger = swagger_auto_schema(
    operation_summary="유저 정보 일부 수정 (PATCH)",
    operation_description="닉네임, 연령, 투자 성향 등 일부 유저 정보를 수정합니다.",
    request_body=UserSerializer(partial=True),
    responses={200: openapi.Response("수정 성공", UserSerializer())},
    tags=TAG,
)

me_delete_swagger = swagger_auto_schema(
    operation_summary="회원 탈퇴 (DELETE)",
    operation_description="현재 로그인된 사용자의 계정을 삭제합니다.",
    responses={200: openapi.Response("삭제 성공")},
    tags=TAG,
)
kakao_login_swagger = swagger_auto_schema(
    operation_summary="카카오 로그인 (POST)",
    operation_description="카카오 access_token을 전달하면 사용자 정보를 조회하고, 최초 로그인 시 회원가입 처리 후 JWT 토큰을 반환합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["access_token"],
        properties={
            "access_token": openapi.Schema(
                type=openapi.TYPE_STRING, description="카카오 인증 access token"
            ),
        },
        example={
            "access_token": "y7BaFULVydBxLpTVJxxy8YhNSv0Y_14RAAAAAQoXEC8AAAGXAzN9MgGXonZVdqHq"
        },
    ),
    responses={
        200: openapi.Response(
            description="로그인 성공",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "user": openapi.Schema(type=openapi.TYPE_OBJECT),  # 간단화
                    "token": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: "잘못된 요청",
        500: "서버 오류",
    },
    tags=["auth"],
)

google_login_swagger = swagger_auto_schema(
    operation_summary="구글 로그인 (POST)",
    operation_description="구글 access_token을 전달하면 사용자 정보를 조회하고, 최초 로그인 시 회원가입 처리 후 JWT 토큰을 반환합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["access_token"],
        properties={
            "access_token": openapi.Schema(
                type=openapi.TYPE_STRING, description="구글 인증 access token"
            ),
        },
        example={"access_token": "ya29.a0AfB_byD_example_token"},
    ),
    responses={
        200: openapi.Response(
            description="로그인 성공",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    "message": openapi.Schema(type=openapi.TYPE_STRING),
                    "user": openapi.Schema(type=openapi.TYPE_OBJECT),  # 간단화
                    "token": openapi.Schema(type=openapi.TYPE_STRING),
                },
            ),
        ),
        400: "잘못된 요청",
        500: "서버 오류",
    },
    tags=["auth"],
)

favorite_get_swagger = swagger_auto_schema(
    operation_summary="찜한 상품 전체 조회 (GET)",
    operation_description="현재 로그인된 사용자가 찜한 예금, 적금, 현물 상품 정보를 모두 조회합니다.",
    responses={200: openapi.Response("조회 성공", UserFavoriteProductsSerializer())},
    tags=TAG,
)

favorite_post_swagger = swagger_auto_schema(
    operation_summary="찜한 상품 추가 또는 해제 (POST)",
    operation_description=(
        "사용자가 특정 상품을 찜하면 찜 항목에 추가되고, "
        "이미 찜한 항목일 경우 해당 항목을 찜 해제합니다. "
        "`type`은 deposit/saving/asset 중 하나여야 하며, `id`는 해당 상품의 ID입니다."
    ),
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["type", "id"],
        properties={
            "type": openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=["deposit", "saving", "asset"],
                description="상품 타입",
            ),
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="상품의 고유 ID"
            ),
        },
        example={"type": "deposit", "id": 1},
    ),
    responses={
        200: openapi.Response(description="찜 추가 또는 해제 결과 메시지"),
        400: "잘못된 요청",
        404: "존재하지 않는 상품",
    },
    tags=TAG,
)

favorite_delete_swagger = swagger_auto_schema(
    operation_summary="찜한 상품 삭제 (DELETE)",
    operation_description="찜한 상품을 완전히 삭제합니다. type과 id를 body로 전달합니다.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=["type", "id"],
        properties={
            "type": openapi.Schema(
                type=openapi.TYPE_STRING,
                enum=["deposit", "saving", "asset"],
                description="상품 타입",
            ),
            "id": openapi.Schema(
                type=openapi.TYPE_INTEGER, description="상품의 고유 ID"
            ),
        },
        example={"type": "asset", "id": 3},
    ),
    responses={200: "찜 항목 삭제 완료", 400: "잘못된 요청"},
    tags=TAG,
)
