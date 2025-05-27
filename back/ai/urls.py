from django.urls import path, include

from .views import recommend_products_view, chat_bot_view

urlpatterns = [
    path("recommend/", recommend_products_view, name="ai-recommend"),
    path("chat/<str:style>/", chat_bot_view, name="ai-chat-bot"),
]
