# accounts/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.adapters import KakaoOAuth2Adapter, CustomGoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from accounts.serializers import (
    UserSerializer,
    UserFavoriteProductsSerializer,
    CustomRegisterSerializer,
)
from swaggers.accounts_swaggers import *
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import RegisterView


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def perform_create(self, serializer):
        response_data = serializer.save(self.request)
        self.user_data = response_data
        self.user = response_data["user"]

    @register_post_swagger
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(self.user_data)
        token = self.user_data.get("key")

        user_data = UserSerializer(self.user).data
        return Response(
            {
                "message": "회원가입 성공",
                "user": user_data,
                "token": token,
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


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


from dj_rest_auth.views import LoginView  # LoginView 임포트


class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            user_data = UserSerializer(request.user).data
            return Response(
                {
                    "message": "로그인 성공",
                    "user": user_data,
                    "token": response.data.get("key"),
                },
                status=status.HTTP_200_OK,
            )
        return response


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    callback_url = "http://localhost:8000/accounts/auth/kakao/login/callback/"
    client_class = OAuth2Client

    @kakao_login_swagger
    def post(self, request, *args, **kwargs):
        print("요청 body:", request.body)
        print("요청 data:", request.data)
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

    @google_login_swagger
    def post(self, request, *args, **kwargs):
        print("요청 body:", request.body)
        print("요청 data:", request.data)
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


class MyFavoriteProductsView(APIView):
    permission_classes = [IsAuthenticated]

    @favorite_get_swagger
    def get(self, request):
        serializer = UserFavoriteProductsSerializer(request.user)
        return Response(serializer.data)

    @favorite_post_swagger
    def post(self, request):
        product_type = request.data.get("type")  # "deposit", "saving", "asset"
        product_id = request.data.get("id")

        if not product_type or not product_id:
            return Response({"error": "type과 id를 모두 전달해야 합니다."}, status=400)

        user = request.user
        added = False

        if product_type == "deposit":
            from products.models import DepositProduct

            product = DepositProduct.objects.filter(id=product_id).first()
            if not product:
                return Response(
                    {"error": "해당 예금 상품이 존재하지 않습니다."}, status=404
                )
            if product in user.favorite_deposits.all():
                user.favorite_deposits.remove(product)
            else:
                user.favorite_deposits.add(product)
                added = True

        elif product_type == "saving":
            from products.models import SavingProduct

            product = SavingProduct.objects.filter(id=product_id).first()
            if not product:
                return Response(
                    {"error": "해당 적금 상품이 존재하지 않습니다."}, status=404
                )
            if product in user.favorite_savings.all():
                user.favorite_savings.remove(product)
            else:
                user.favorite_savings.add(product)
                added = True

        elif product_type == "asset":
            from products.models import SpotAssetProduct

            product = SpotAssetProduct.objects.filter(id=product_id).first()
            if not product:
                return Response(
                    {"error": "해당 현물 상품이 존재하지 않습니다."}, status=404
                )
            if product in user.favorite_assets.all():
                user.favorite_assets.remove(product)
            else:
                user.favorite_assets.add(product)
                added = True
        else:
            return Response({"error": "잘못된 상품 타입입니다."}, status=400)

        return Response({"message": "찜 추가됨" if added else "찜 해제됨"})

    @favorite_delete_swagger
    def delete(self, request):
        product_type = request.data.get("type")  # "deposit", "saving", "asset"
        product_id = request.data.get("id")

        if not product_type or not product_id:
            return Response({"error": "type과 id를 모두 전달해야 합니다."}, status=400)

        user = request.user

        if product_type == "deposit":
            from products.models import DepositProduct

            product = DepositProduct.objects.filter(id=product_id).first()
            if product:
                user.favorite_deposits.remove(product)

        elif product_type == "saving":
            from products.models import SavingProduct

            product = SavingProduct.objects.filter(id=product_id).first()
            if product:
                user.favorite_savings.remove(product)

        elif product_type == "asset":
            from products.models import SpotAssetProduct

            product = SpotAssetProduct.objects.filter(id=product_id).first()
            if product:
                user.favorite_assets.remove(product)

        else:
            return Response({"error": "잘못된 상품 타입입니다."}, status=400)

        return Response({"message": "찜 항목 삭제 완료"})
