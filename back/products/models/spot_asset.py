from django.db import models
from .deposit import Bank

class SpotAssetProduct(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="spot_asset_products")

    name = models.CharField(max_length=100)
    description = models.TextField()
    purchase_url = models.URLField()
    price = models.BigIntegerField()

    def __str__(self):
        return f"[현물] {self.name}"
