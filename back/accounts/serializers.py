import logging
from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from products.serializers import (
    DepositProductSerializer,
    SavingProductSerializer,
    SpotAssetProductSerializer,
)
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
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


import uuid  # uuid 모듈 추가


class CustomRegisterSerializer(RegisterSerializer):
    # username 필드를 제거
    username = None

    age = serializers.IntegerField(required=False, allow_null=True)
    # name 필드를 필수로 받도록 변경
    name = serializers.CharField(max_length=30, required=True)
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
        # nickname을 name과 동일하게 설정
        data["name"] = self.validated_data.get("name")
        data["nickname"] = self.validated_data.get(
            "name"
        )  # nickname을 name과 동일하게 설정
        return data

    def save(self, request):
        logger.info("📌 CustomRegisterSerializer.save() 호출됨")
        try:
            # super().save() 호출 전에 username을 설정
            # AbstractUser의 username 필드는 필수이므로, 임시로 고유한 값을 할당
            # 이 값은 이후에 실제 uid로 대체될 수 있음
            # 여기서는 uuid를 사용하여 고유한 username을 생성
            temp_username = str(uuid.uuid4())
            self.validated_data["username"] = temp_username

            user = super().save(request)
            logger.info(f"📌 save() - super().save() 후 user.username: {user.username}")
            logger.info(f"📌 save() - super().save() 후 user.name: {user.name}")
            logger.info(f"📌 save() - super().save() 후 user.nickname: {user.nickname}")

            age_value = self.validated_data.get("age", None)
            logger.info(f"📌 save() - age_value: {age_value}")
            user.age = age_value

            # name과 nickname을 validated_data에서 가져오거나 name으로 설정
            user.name = self.validated_data.get("name")
            user.nickname = self.validated_data.get(
                "name"
            )  # nickname을 name과 동일하게 설정

            # username을 uid로 설정 (예: email을 기반으로 한 uid)
            # 여기서는 간단하게 email을 username으로 사용하거나, uuid를 다시 생성
            # 사용자의 요청에 따라 카카오 로그인처럼 uid로 만드는 것이 베스트이므로,
            # 여기서는 email을 기반으로 한 uid를 생성하거나, uuid를 사용
            # 일단은 email을 username으로 설정하고, 필요시 uid 생성 로직 추가
            user.username = user.email  # 또는 str(uuid.uuid4())

            user.save()
            logger.info(
                f"📌 save() - 사용자 저장 완료: {user.email}, name: {user.name}, nickname: {user.nickname}, age: {user.age}"
            )
            # dj_rest_auth의 RegisterSerializer가 기대하는 형식으로 반환
            # Token을 직접 생성하여 반환 딕셔너리에 포함
            token, created = Token.objects.get_or_create(user=user)
            return {"user": user, "token": token, "key": token.key}
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
