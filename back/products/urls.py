from django.urls import path
from .views import ProductListView
from .views import DepositListView

urlpatterns = [
   path("", ProductListView.as_view()), 
   path("deposit/", DepositListView.as_view()), 
]
