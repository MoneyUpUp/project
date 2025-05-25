from django.db import models


class SpotAssetProduct(models.Model):
    name = models.CharField(max_length=20)  # gold, silver, oil 등

    def __str__(self):
        return self.name


class SpotAssetPrice(models.Model):
    product = models.ForeignKey(
        SpotAssetProduct, on_delete=models.CASCADE, related_name="price_history"
    )
    date = models.DateField()
    close_price = models.FloatField()

    class Meta:
        unique_together = ("product", "date")  # ✔ 수정
        ordering = ["-date"]

    def __str__(self):
        return f"{self.product.name} - {self.date} : {self.close_price}"  # ✔ 수정
