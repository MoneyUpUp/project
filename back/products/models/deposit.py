from django.db import models
from products.models.bank import Bank


class DepositProduct(models.Model):
    bank = models.ForeignKey(
        Bank, on_delete=models.CASCADE, related_name="deposit_products"
    )

    dcls_month = models.CharField(max_length=6)
    fin_prdt_cd = models.CharField(max_length=20)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.CharField(max_length=255)
    mtrt_int = models.TextField()
    spcl_cnd = models.CharField(max_length=255)
    join_deny = models.CharField(max_length=255)
    join_member = models.CharField(max_length=255)
    etc_note = models.CharField(max_length=255)
    max_limit = models.BigIntegerField(null=True, blank=True)
    dcls_strt_day = models.DateField(null=True, blank=True)
    dcls_end_day = models.DateField(null=True, blank=True)
    fin_co_subm_day = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"[{self.bank.kor_co_nm}] {self.fin_prdt_nm}"


class DepositOption(models.Model):
    product = models.ForeignKey(
        DepositProduct, on_delete=models.CASCADE, related_name="options"
    )

    intr_rate_type = models.CharField(max_length=10)
    intr_rate_type_nm = models.CharField(max_length=30)
    save_trm = models.PositiveIntegerField()
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2)
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.product.fin_prdt_nm} - {self.save_trm}개월"
