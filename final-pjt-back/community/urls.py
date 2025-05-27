from django.urls import path
from community.views import *

urlpatterns = [
    # 게시글
    path("articles/", ArticleListView.as_view()),
    path("articles/<int:article_id>/", ArticleView.as_view()),
    # 댓글
    path("articles/<int:article_id>/comments/", CommentListView.as_view()),
    path("comments/<int:comment_id>/", CommentView.as_view()),
]
