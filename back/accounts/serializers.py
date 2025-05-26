import logging
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

logger = logging.getLogger(__name__)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
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


class CustomRegisterSerializer(RegisterSerializer):
    age = serializers.IntegerField(required=False, allow_null=True)
    name = serializers.CharField(max_length=30, required=False, allow_blank=True)
    nickname = serializers.CharField(max_length=30, required=False, allow_blank=True)
    password2 = serializers.CharField(write_only=True, required=False)

    def validate(self, data):
        print("📌 CustomRegisterSerializer.validate() 호출됨")
        print("📌 validate() - 초기 data:", data)
        # password2가 없으면 자동 복사
        data["password2"] = data.get("password1")
        validated_data = super().validate(data)
        print("📌 validate() - super().validate() 후 data:", validated_data)
        return validated_data

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data["age"] = self.validated_data.get("age", None)  # age가 없으면 None으로 설정
        # name과 nickname이 제공되지 않으면 username으로 설정
        data["name"] = self.validated_data.get("name", data.get("username"))
        data["nickname"] = self.validated_data.get("nickname", data.get("username"))
        return data

    def save(self, request):
        logger.info("📌 CustomRegisterSerializer.save() 호출됨")
        try:
            user = super().save(request)
            logger.info(f"📌 save() - super().save() 후 user.username: {user.username}")
            logger.info(f"📌 save() - super().save() 후 user.name: {user.name}")
            logger.info(f"📌 save() - super().save() 후 user.nickname: {user.nickname}")

            age_value = self.validated_data.get("age", None)
            logger.info(f"📌 save() - age_value: {age_value}")
            user.age = age_value

            # name과 nickname을 validated_data에서 가져오거나 username으로 설정
            user.name = self.validated_data.get("name", user.username)
            user.nickname = self.validated_data.get("nickname", user.username)

            user.save()
            logger.info(
                f"📌 save() - 사용자 저장 완료: {user.username}, name: {user.name}, nickname: {user.nickname}, age: {user.age}"
            )
            return user
        except Exception as e:
            logger.error(f"❌ 예외 발생: {e}", exc_info=True)
            raise e


class UserFavoriteProductsSerializer(serializers.ModelSerializer):
    favorite_deposits = DepositProductSerializer(many=True, read_only=True)
    favorite_savings = SavingProductSerializer(many=True, read_only=True)
    favorite_assets = SpotAssetProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["favorite_deposits", "favorite_savings", "favorite_assets"]

    class Meta:
        model = User
        fields = ["favorite_deposits", "favorite_savings", "favorite_assets"]

    class Meta:
        model = User
        fields = ["favorite_deposits", "favorite_savings", "favorite_assets"]
