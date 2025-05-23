from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status


from community.serializers import *

from swaggers.community_swaggers import *


class ArticleView(APIView):
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


class ArticleDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @article_detail_get
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # @article_update_put
    # def put(self, request, article_id):
    #     article = get_object_or_404(Article, id=article_id)
    #     if request.user != article.author:
    #         return Response({"detail": "권한이 없습니다."}, status=403)
    #     serializer = ArticleSerializer(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=400)

    @article_update_patch
    def patch(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user != article.author:
            return Response({"detail": "권한이 없습니다."}, status=403)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @article_delete
    def delete(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user != article.author:
            return Response({"detail": "권한이 없습니다."}, status=403)
        article.delete()
        return Response({"message": "삭제 완료"}, status=204)


class CommentListCreateView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @comment_list_get
    def get(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        comments = article.comments.all().order_by("-created_at")
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @comment_create_post
    def post(self, request, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article=article)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class CommentDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    @comment_update_put
    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author != request.user:
            return Response({"detail": "권한이 없습니다."}, status=403)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @comment_update_patch
    def patch(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author != request.user:
            return Response({"detail": "권한이 없습니다."}, status=403)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @comment_delete
    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        if comment.author != request.user:
            return Response({"detail": "권한이 없습니다."}, status=403)
        comment.delete()
        return Response({"message": "댓글 삭제 완료"}, status=204)
