from django.apps import AppConfig
import threading


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        import os

        if os.environ.get("RUN_MAIN") != "true":
            return

        # ✅ 이 시점에만 import 해야 안전함
        from products.utils.update_checker import should_update, mark_updated
        from products.api.fin_api import get_saving_api, get_deposit_api
        from products.api.yfinance_api import save_asset_prices, TICKER_MAP

        def run_on_start():
            if should_update("saving"):
                get_saving_api()
            if should_update("deposit"):
                get_deposit_api()

            # yfinance_api의 ticker_map 데이터를 DB에 저장
            if should_update("spot_asset"):
                for name in TICKER_MAP.keys():
                    save_asset_prices(name)
                mark_updated("spot_asset")

        threading.Thread(target=run_on_start).start()
