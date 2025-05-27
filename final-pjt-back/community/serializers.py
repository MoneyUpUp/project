from rest_framework import serializers
from community.models import Article, Comment
from accounts.models import User


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "content", "created_at", "updated_at", "author_name"]
        read_only_fields = ["author", "created_at", "updated_at"]


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "article", "content", "created_at", "updated_at", "author_name"]
        read_only_fields = ["author", "created_at", "updated_at"]
