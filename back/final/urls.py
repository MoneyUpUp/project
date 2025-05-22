from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger 스키마 뷰 설정
schema_view = get_schema_view(
    openapi.Info(
        title="MoneyUp API",
        default_version="v1",
        description="금융 상품 비교 플랫폼",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    #
    path("accounts/", include("accounts.urls")),
    # path("community/", include("community.urls")),
    path("products/", include("products.urls")),
    #
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/signup/", include("dj_rest_auth.registration.urls")),
    # swagger
    # Swagger UI
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # ReDoc
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # JSON/YAML 형태로도 제공
    path("swagger.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger.yaml", schema_view.without_ui(cache_timeout=0), name="schema-yaml"),
]
