# from django.db import models


# from django.db import models


# # 금융회사 (이미 존재하면 유지)
# class Bank(models.Model):
#     fin_co_no = models.CharField(max_length=10, unique=True)  # 금융회사 코드
#     kor_co_nm = models.CharField(max_length=50)  # 금융회사명

#     def __str__(self):
#         return self.kor_co_nm


# # 예금 상품 정보
# class Product(models.Model):
#     bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="products")

#     dcls_month = models.CharField(max_length=6)  # 공시 제출 월
#     fin_prdt_cd = models.CharField(max_length=20)  # 금융상품 코드
#     fin_prdt_nm = models.CharField(max_length=100)  # 금융상품명
#     join_way = models.TextField()  # 가입 방법
#     mtrt_int = models.TextField()  # 만기 후 이자율 설명
#     spcl_cnd = models.TextField()  # 우대 조건
#     join_deny = models.TextField()  # 가입 제한 여부
#     join_member = models.TextField()  # 가입 대상
#     etc_note = models.TextField()  # 기타 유의사항
#     max_limit = models.BigIntegerField(null=True, blank=True)  # 가입 금액 한도
#     dcls_strt_day = models.DateField()  # 공시 시작일
#     dcls_end_day = models.DateField(null=True, blank=True)  # 공시 종료일
#     fin_co_subm_day = models.DateTimeField()  # 금융회사 제출 일시

#     def __str__(self):
#         return f"{self.bank.kor_co_nm} - {self.fin_prdt_nm}"


# # 금리 조건의 공통 필드를 추출한 추상 클래스
# class InterestBase(models.Model):
#     # 연결된 금융상품
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

#     # 저축 금리 유형 코드 (ex: S, F 등)
#     intr_rate_type = models.CharField(max_length=10)

#     # 저축 금리 유형명 (ex: 단리, 복리 등)
#     intr_rate_type_nm = models.CharField(max_length=30)

#     # 저축 기간 (ex: 6, 12, 24개월 등)
#     save_trm = models.PositiveIntegerField()

#     # 기본 금리 (% 단위)
#     intr_rate = models.FloatField()

#     # 최고 우대 금리 (% 단위)
#     intr_rate2 = models.FloatField()

#     class Meta:
#         abstract = True


# # 예금 상품 금리 옵션
# class DepositOption(InterestBase):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name="deposit_options"
#     )

#     def __str__(self):
#         return f"[예금] {self.product.fin_prdt_nm} - {self.save_trm}개월"


# # 적금 상품 금리 옵션 + 적립 유형 정보 포함
# class InstallmentOption(InterestBase):
#     product = models.ForeignKey(
#         Product, on_delete=models.CASCADE, related_name="installment_options"
#     )

#     # 적립 유형 코드 (ex: S, M 등)
#     rsrv_type = models.CharField(max_length=10)

#     # 적립 유형명 (ex: 정액적립식, 자유적립식)
#     rsrv_type_nm = models.CharField(max_length=30)

#     def __str__(self):
#         return f"[적금] {self.product.fin_prdt_nm} - {self.save_trm}개월 ({self.rsrv_type_nm})"
from .models import *