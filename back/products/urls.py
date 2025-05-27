from django.urls import path
from .views import ProductListView, CommodityHistoryView

urlpatterns = [
    path("", ProductListView.as_view()),
    path("spotAssets/<str:commodity_name>/", CommodityHistoryView.as_view()),
]
