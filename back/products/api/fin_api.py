import requests
import os
from products.models import Bank, DepositProduct, DepositOption
from datetime import datetime
from pprint import pprint

def fetch_financial_products():
    api_key = os.environ.get("FIN_API_KEY")
    response = requests.get(
        f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1"
    )
    return response.json()


def get_deposit_api():
    data = fetch_financial_products()
    base_list = data["result"]["baseList"]
    option_list = data["result"]["optionList"]

    for item in base_list:
        bank, _ = Bank.objects.get_or_create(
            fin_co_no=item["fin_co_no"],
            defaults={"kor_co_nm": item["kor_co_nm"]}
        )

        product, _ = DepositProduct.objects.get_or_create(
            bank=bank,
            fin_prdt_cd=item["fin_prdt_cd"],
            defaults={
                "dcls_month": item["dcls_month"],
                "fin_prdt_nm": item["fin_prdt_nm"],
                "join_way": item["join_way"],
                "mtrt_int": item["mtrt_int"],
                "spcl_cnd": item["spcl_cnd"],
                "join_deny": item["join_deny"],
                "join_member": item["join_member"],
                "etc_note": item["etc_note"],
                "max_limit": item.get("max_limit"),
                "dcls_strt_day": datetime.strptime(item["dcls_strt_day"], "%Y%m%d").date(),
                "dcls_end_day": datetime.strptime(item["dcls_end_day"], "%Y%m%d").date() if item.get("dcls_end_day") else None,
                "fin_co_subm_day": datetime.strptime(item["fin_co_subm_day"], "%Y%m%d%H%M"),
            }
        )

    for opt in option_list:
        try:
            bank = Bank.objects.get(fin_co_no=opt["fin_co_no"])
            product = DepositProduct.objects.get(bank=bank, fin_prdt_cd=opt["fin_prdt_cd"])

            DepositOption.objects.update_or_create(
                product=product,
                intr_rate_type=opt["intr_rate_type"],
                save_trm=int(opt["save_trm"]),
                defaults={
                    "intr_rate_type_nm": opt["intr_rate_type_nm"],
                    "intr_rate": float(opt.get("intr_rate") or 0.0),
                    "intr_rate2": float(opt.get("intr_rate2") or 0.0),
                }
            )
        except (Bank.DoesNotExist, DepositProduct.DoesNotExist):
            print(f"[오류] Product 또는 Bank 없음 - {opt['fin_prdt_cd']} / {opt['fin_co_no']}")
