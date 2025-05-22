# accounts/urls.py
from django.urls import path
from .views import AuthCheckView

urlpatterns = [
    path("check/", AuthCheckView.as_view()),
]
