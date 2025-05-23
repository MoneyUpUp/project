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

    class Meta:
        model = DepositProduct
        fields = "__all__"


class SavingProductSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    options = SavingOptionSerializer(many=True)

    class Meta:
        model = SavingProduct
        fields = "__all__"
