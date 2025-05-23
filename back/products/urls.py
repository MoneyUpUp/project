from django.urls import path
from .views import *

urlpatterns = [
    path(
        "",
        AllListView.as_view(),
        name="product-all",
    ),
    path(
        "deposit/",
        DepositListView.as_view(),
        name="product-deposit-list",
    ),
    path(
        "saving/",
        SavingListView.as_view(),
        name="product-saving-list",
    ),
]
