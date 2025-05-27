from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from accounts.views import KakaoLogin, GoogleLogin, CustomLoginView, CustomRegisterView

from accounts.urls import urlpatterns as accounts_urls
from products.urls import urlpatterns as products_urls
from community.urls import urlpatterns as community_urls
from ai.urls import urlpatterns as ai_urls

api_urlpatterns = (
    accounts_urls
    + products_urls
    + community_urls
    + ai_urls
    + [
        path("auth/kakao/login/", KakaoLogin.as_view()),
        path("auth/google/login/", GoogleLogin.as_view()),
        path("auth/login/", CustomLoginView.as_view()),
        path("auth/signup/", CustomRegisterView.as_view()),
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
