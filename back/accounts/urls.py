from django.urls import path, include
from accounts.views import MeView, KakaoLogin, GoogleLogin, MyFavoriteProductsView

urlpatterns = [
    # 인증 관련 (로그인, 회원가입, 소셜 로그인 등)
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/signup/", include("dj_rest_auth.registration.urls")),
    path("auth/kakao/login/", KakaoLogin.as_view()),
    path("auth/google/login/", GoogleLogin.as_view()),
    # 사용자 정보
    path("me/", MeView.as_view(), name="accounts-me"),
    path("me/favorites/", MyFavoriteProductsView.as_view(), name="user-favorites"),
]
