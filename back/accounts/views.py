# accounts/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from accounts.serializers import UserSerializer
from swaggers.accounts_swaggers import *

# test
class MeView(APIView):
    permission_classes = [IsAuthenticated]

    @me_get_swagger
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @me_patch_swagger
    def patch(self, request):
        serializer = UserSerializer(
            instance=request.user, data=request.data, partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "정보 수정 완료", "user": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @me_delete_swagger
    def delete(self, request):
        request.user.delete()
        return Response({"message": "회원 탈퇴 완료"})
