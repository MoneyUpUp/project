from django.db import models


class Bank(models.Model):
    fin_co_no = models.CharField(max_length=10, unique=True)
    kor_co_nm = models.CharField(max_length=50)

    def __str__(self):
        return self.kor_co_nm
