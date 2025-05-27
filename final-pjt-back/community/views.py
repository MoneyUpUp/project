from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


from community.serializers import ArticleSerializer, CommentSerializer
from community.models import Article, Comment
from swaggers.community_swaggers import *


def check_ownership(user, obj):
    if obj.author != user:
        raise PermissionDenied("권한이 없습니다.")


class ArticleListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @article_list_get
    def get(self, request):
        articles = Article.objects.all().order_by("-created_at")
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @article_create_post
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ArticleView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @article_detail_get
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    @article_update_patch
    def patch(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        check_ownership(request.user, article)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @article_delete
    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        check_ownership(request.user, article)
        article.delete()
        return Response({"message": "삭제 완료"}, status=204)


class CommentListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @comment_list_get
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        comments = article.comments.all().order_by("-created_at")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @comment_update_put
    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        check_ownership(request.user, comment)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @comment_update_patch
    def patch(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        check_ownership(request.user, comment)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @comment_delete
    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        check_ownership(request.user, comment)
        comment.delete()
        return Response({"message": "댓글 삭제 완료"}, status=204)

    @comment_create_post
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article=article)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
