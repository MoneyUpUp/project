from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework import serializers
from .models import User
from products.serializers import (
    DepositProductSerializer,
    SavingProductSerializer,
    SpotAssetProductSerializer,
)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",  # 읽기 전용
            "email",
            "name",
            "nickname",
            "age",
            "profile_image",
            "annual_income",
            "invest_type",
            "preferred_term",
            "favorite_deposits",
            "favorite_savings",
            "favorite_assets",
        ]
        read_only_fields = ["username"]


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=True)

    # password2를 명시적으로 남겨두되 required=False로 지정
    password2 = serializers.CharField(write_only=True, required=False)

    def validate(self, data):
        # password2가 없으면 자동 복사
        data["password2"] = data.get("password1")
        return super().validate(data)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["age"] = self.validated_data.get("age")
        return data

    def save(self, request):
        user = super().save(request)
        user.age = self.validated_data.get("age")
        user.nickname = user.username  # 자동 닉네임
        user.save()
        return user


class UserFavoriteProductsSerializer(serializers.ModelSerializer):
    favorite_deposits = DepositProductSerializer(many=True, read_only=True)
    favorite_savings = SavingProductSerializer(many=True, read_only=True)
    favorite_assets = SpotAssetProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["favorite_deposits", "favorite_savings", "favorite_assets"]
