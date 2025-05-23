from django.db import models
from .deposit import Bank

class SavingProduct(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="saving_products")

    dcls_month = models.CharField(max_length=6)
    fin_prdt_cd = models.CharField(max_length=20)
    fin_prdt_nm = models.CharField(max_length=100)
    join_way = models.TextField()
    mtrt_int = models.TextField()
    spcl_cnd = models.TextField()
    join_deny = models.TextField()
    join_member = models.TextField()
    etc_note = models.TextField()
    max_limit = models.BigIntegerField(null=True, blank=True)
    dcls_strt_day = models.DateField()
    dcls_end_day = models.DateField(null=True, blank=True)
    fin_co_subm_day = models.DateTimeField()

    def __str__(self):
        return f"[적금] {self.fin_prdt_nm}"


class SavingOption(models.Model):
    product = models.ForeignKey(SavingProduct, on_delete=models.CASCADE, related_name="options")

    intr_rate_type = models.CharField(max_length=10)
    intr_rate_type_nm = models.CharField(max_length=30)
    save_trm = models.PositiveIntegerField()
    intr_rate = models.DecimalField(max_digits=5, decimal_places=2)
    intr_rate2 = models.DecimalField(max_digits=5, decimal_places=2)

    rsrv_type = models.CharField(max_length=10)
    rsrv_type_nm = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.product.fin_prdt_nm} - {self.save_trm}개월 ({self.rsrv_type_nm})"
