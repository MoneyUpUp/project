from django.urls import path
from community.views import *

urlpatterns = [
    # 게시글
    path(
        "articles/",
        ArticleView.as_view(),
        name="article-list-create",
    ),
    path(
        "articles/<int:article_id>/",
        ArticleDetailView.as_view(),
        name="article-detail",
    ),
    # 댓글
    path(
        "articles/<int:article_id>/comments/",
        CommentListCreateView.as_view(),
        name="comment-list-create",
    ),
    path(
        "comments/<int:comment_id>/",
        CommentDetailView.as_view(),
        name="comment-detail",
    ),
]
