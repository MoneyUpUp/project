from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",  # 읽기 전용
            "email",  # 읽기 전용
            "name",
            "nickname",
            "age",
            "profile_image",
            "annual_income",
            "invest_type",
            "preferred_term",
        ]
        read_only_fields = ["username", "email"]
