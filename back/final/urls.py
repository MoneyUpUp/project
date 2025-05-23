from django.contrib import admin
from django.urls import path, include

from swaggers.schema_view import schema_view  # 분리된 Swagger 스키마 불러오기

urlpatterns = [
    path("admin/", admin.site.urls),
    #
    path("accounts/", include("accounts.urls")),
    path("community/", include("community.urls")),
    path("products/", include("products.urls")),
    #
    path("auth/", include("dj_rest_auth.urls")),
    path("auth/signup/", include("dj_rest_auth.registration.urls")),
    # swagger
    # Swagger UI
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
    # ReDoc
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
    # JSON/YAML 형태로도 제공
    path("swagger.json", schema_view.without_ui(cache_timeout=0)),
    path("swagger.yaml", schema_view.without_ui(cache_timeout=0)),
]
