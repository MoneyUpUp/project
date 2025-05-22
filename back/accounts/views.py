# accounts/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from .swaggers import (
    about_user_patch,
    about_user_put,
    about_user_delete,
)


class AboutUser(APIView):
    permission_classes = [IsAuthenticated]

    @about_user_patch
    def patch(self, request):
        user = request.user
        user.nickname = request.data.get("nickname", user.nickname)
        user.save()
        return Response({"message": "정보 수정 완료 (일부)"})

    @about_user_put
    def put(self, request):
        user = request.user
        user.nickname = request.data.get("nickname", "")
        user.save()
        return Response({"message": "정보 수정 완료 (전체)"})

    @about_user_delete
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "회원 탈퇴 완료"})
