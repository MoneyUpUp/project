from django.urls import path, include
from accounts.views import MeView, MyFavoriteProductsView

urlpatterns = [
    # 사용자 정보
    path("me/", MeView.as_view()),
    path("me/favorites/", MyFavoriteProductsView.as_view()),
]
