from django.contrib import admin
from django.urls import path, include

from swaggers.schema_view import schema_view
from accounts.views import (
    KakaoLogin,
    GoogleLogin,
    CustomRegisterView,
    CustomLoginView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # 앱 URL 연결
    path("accounts/", include("accounts.urls")),
    path("community/", include("community.urls")),
    path("products/", include("products.urls")),
    path("ai/", include("ai.urls")),
    # 인증 관련 URL (커스텀 뷰 우선 등록)
    path("auth/login/", CustomLoginView.as_view()),
    path("auth/signup/", CustomRegisterView.as_view()),
    path("auth/kakao/login/", KakaoLogin.as_view()),
    path("auth/google/login/", GoogleLogin.as_view()),
    path("auth/", include("dj_rest_auth.urls")),
    # Swagger / ReDoc UI
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
]
