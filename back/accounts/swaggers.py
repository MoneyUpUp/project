from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from accounts.serializers import UserSerializer

about_user_patch = swagger_auto_schema(
    operation_summary="유저 정보 일부 수정 (PATCH)",
    operation_description="닉네임 등 일부 유저 정보를 수정합니다.",
    request_body=UserSerializer(partial=True),
    responses={200: openapi.Response("수정 완료")},
)

about_user_put = swagger_auto_schema(
    operation_summary="유저 정보 전체 수정 (PUT)",
    operation_description="유저 정보를 전부 수정합니다.",
    request_body=UserSerializer(),
    responses={200: openapi.Response("전체 수정 완료")},
)

about_user_delete = swagger_auto_schema(
    operation_summary="회원 탈퇴 (DELETE)",
    operation_description="현재 로그인된 사용자를 삭제합니다.",
    responses={200: openapi.Response("삭제 완료")},
)
