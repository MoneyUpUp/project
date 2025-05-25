from django.db import models


class SpotAssetProduct(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    purchase_url = models.URLField()
    price = models.BigIntegerField()

    def __str__(self):
        return f"[{self.code}] {self.name}"


class SpotAssetPrice(models.Model):
    product = models.ForeignKey(
        SpotAssetProduct, on_delete=models.CASCADE, related_name="price_history"
    )
    date = models.DateField()
    close = models.FloatField()
    volume = models.FloatField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()

    class Meta:
        unique_together = ("product", "date")
        ordering = ["-date"]

    def __str__(self):
        return f"{self.product.asset_code} @ {self.date}"
