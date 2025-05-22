# accounts/urls.py
from django.urls import path
from .views import AboutUser

urlpatterns = [
    path("update/", AboutUser.as_view(), name="about-user"),
]
