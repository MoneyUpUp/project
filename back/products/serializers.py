from rest_framework import serializers
from products.models import Bank, DepositProduct, DepositOption

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ["fin_co_no", "kor_co_nm"]

class DepositOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOption
        exclude = ["id", "product"]

class DepositProductSerializer(serializers.ModelSerializer):
    bank = BankSerializer()
    options = DepositOptionSerializer(many=True)

    class Meta:
        model = DepositProduct
        fields = "__all__"
