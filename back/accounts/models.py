from django.db import models
from django.contrib.auth.models import AbstractUser
from .constants import INVEST_TYPE_CHOICES, PREFERRED_TERM_CHOICES


class User(AbstractUser):
    # 필수 정보
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    name = models.CharField(max_length=30, blank=True)
    nickname = models.CharField(max_length=30, blank=True)
    email = models.EmailField()
    age = models.PositiveIntegerField(null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )

    # 금융 관련 정보
    # 연봉
    annual_income = models.PositiveIntegerField(null=True, blank=True)

    # 투자 성향
    invest_type = models.CharField(
        max_length=1, choices=INVEST_TYPE_CHOICES, null=True, blank=True
    )

    # 희망 투자 기간
    preferred_term = models.CharField(
        max_length=1, choices=PREFERRED_TERM_CHOICES, null=True, blank=True
    )

    # 찜
    favorite_deposits = models.ManyToManyField(
        "products.DepositProduct", blank=True, related_name="liked_by_users"
    )
    favorite_savings = models.ManyToManyField(
        "products.SavingProduct", blank=True, related_name="liked_by_users"
    )
    favorite_assets = models.ManyToManyField(
        "products.SpotAssetProduct", blank=True, related_name="liked_by_users"
    )

    def __str__(self):
        return self.username
