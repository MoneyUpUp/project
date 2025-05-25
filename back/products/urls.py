from django.urls import path
from .views import *

urlpatterns = [
    path(
        "",
        ProductListView.as_view(),
        name="product-all",
    ),
    path(
        "spotAssets/<str:commodity_name>/",
        CommodityHistoryView.as_view(),
        name="commodity-history",
    ),
]
