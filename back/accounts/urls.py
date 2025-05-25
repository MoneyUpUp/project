from django.urls import path, include
from accounts.views import MeView,  MyFavoriteProductsView

urlpatterns = [
    # 사용자 정보
    path("me/", MeView.as_view(), name="accounts-me"),
    path("me/favorites/", MyFavoriteProductsView.as_view(), name="user-favorites"),
]
