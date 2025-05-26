from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView

from accounts.views import *
from products.views import *
from community.views import *
from ai.views import *  # ai.views 추가

from accounts.urls import urlpatterns as accounts_urls
from products.urls import urlpatterns as products_urls
from community.urls import urlpatterns as community_urls
from ai.urls import urlpatterns as ai_urls  # ai.urls 추가

api_urlpatterns = (
    accounts_urls
    + products_urls
    + community_urls
    + ai_urls  # ai_urls 추가
    + [
        path("auth/kakao/login/", KakaoLogin.as_view()),
        path("auth/google/login/", GoogleLogin.as_view()),
        path("auth/login/", LoginView.as_view(), name="auth-login"),
        path("auth/logout/", LogoutView.as_view(), name="auth-logout"),
        path("auth/signup/", RegisterView.as_view(), name="auth-signup"),
    ]
)

# Swagger 스키마 뷰 설정
schema_view = get_schema_view(
    openapi.Info(
        title="MoneyUp API",
        default_version="v1",
        description="금융 상품 비교 플랫폼",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=api_urlpatterns,
)
