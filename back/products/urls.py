from django.urls import path
from .views import DepositListView, SavingListView

urlpatterns = [
    path("deposit/", DepositListView.as_view()),
    path("saving/", SavingListView.as_view()),
]
