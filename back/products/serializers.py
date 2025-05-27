from rest_framework import serializers
from products.models import *


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ["fin_co_no", "kor_co_nm"]


class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        exclude = ["id", "product"]


class SavingOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOption
        exclude = ["id", "product"]


class DepositProductSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    options = DepositOptionSerializer(many=True)
    type = serializers.CharField(default="deposit")

    class Meta:
        model = DepositProduct
        fields = "__all__"
        extra_fields = ["type"]


class SavingProductSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    options = SavingOptionSerializer(many=True)
    type = serializers.CharField(default="saving")

    class Meta:
        model = SavingProduct
        fields = "__all__"
        extra_fields = ["type"]


class SpotAssetProductSerializer(serializers.ModelSerializer):
    # bank = BankSerializer()
    type = serializers.CharField(default="spotAsset")

    class Meta:
        model = SpotAssetProduct
        fields = "__all__"
        extra_fields = ["type"]


class ProductListResponseSerializer(serializers.Serializer):
    deposit_products = DepositProductSerializer(many=True)
    saving_products = SavingProductSerializer(many=True)
