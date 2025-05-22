
from django.urls import path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from dj_rest_auth.views import LoginView, LogoutView
from dj_rest_auth.registration.views import RegisterView

from accounts.views import MeView

# Swagger 스키마 뷰 설정
schema_view = get_schema_view(
    openapi.Info(
        title="MoneyUp API",
        default_version="v1",
        description="금융 상품 비교 플랫폼",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
        patterns=[
        path("accounts/me/", MeView.as_view()),
        path("auth/login/", LoginView.as_view()),
        path("auth/logout/", LogoutView.as_view()),
        path("auth/signup/", RegisterView.as_view()),
    ],
)
