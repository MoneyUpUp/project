from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accounts.serializers import UserSerializer

TAG = ["accounts"]

# 유저 정보 조회 (GET)
me_get_swagger = swagger_auto_schema(
    operation_summary="유저 정보 조회 (GET)",
    operation_description="현재 로그인한 사용자의 전체 정보를 조회합니다.",
    responses={200: openapi.Response("조회 성공", UserSerializer())},
    tags=TAG,
)

# 유저 정보 일부 수정 (PATCH)
me_patch_swagger = swagger_auto_schema(
    operation_summary="유저 정보 일부 수정 (PATCH)",
    operation_description="닉네임, 연령, 투자 성향 등 일부 유저 정보를 수정합니다.",
    request_body=UserSerializer(partial=True),
    responses={200: openapi.Response("수정 성공", UserSerializer())},
    tags=TAG,
)

# 유저 탈퇴 (DELETE)
me_delete_swagger = swagger_auto_schema(
    operation_summary="회원 탈퇴 (DELETE)",
    operation_description="현재 로그인된 사용자의 계정을 삭제합니다.",
    responses={200: openapi.Response("삭제 성공")},
    tags=TAG,
)
