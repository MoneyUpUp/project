# accounts/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accounts.adapters import KakaoOAuth2Adapter, CustomGoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from accounts.serializers import UserSerializer, UserFavoriteProductsSerializer
from swaggers.accounts_swaggers import *
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


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
    print(123)
    
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


class MyFavoriteProductsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserFavoriteProductsSerializer(request.user)
        return Response(serializer.data)

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
