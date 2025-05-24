# accounts/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.adapters import KakaoOAuth2Adapter, CustomGoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from accounts.serializers import UserSerializer
from swaggers.accounts_swaggers import *
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


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


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/auth/kakao/login/callback/"
    client_class = OAuth2Client

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user_data = UserSerializer(request.user).data
            return Response(
                {
                    "message": "로그인 성공",
                    "user": user_data,
                    "token": response.data.get("key"),
                }
            )
        return response


class GoogleLogin(SocialLoginView):
    adapter_class = CustomGoogleOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/auth/google/login/callback/"
    client_class = OAuth2Client
