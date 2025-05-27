from django.apps import AppConfig
import threading
import certifi
import os
import logging

logger = logging.getLogger(__name__)


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

    def ready(self):
        os.environ["SSL_CERT_FILE"] = certifi.where()
        if os.environ.get("RUN_MAIN") != "true":
            return

        from products.utils.update_checker import should_update, mark_updated
        from products.api.fin_api import get_saving_api, get_deposit_api
        from products.api.yfinance_api import save_asset_prices, TICKER_MAP

        def run_on_start():
            try:
                if should_update("saving"):
                    get_saving_api()
                if should_update("deposit"):
                    get_deposit_api()
                if should_update("spot_asset"):
                    for name in TICKER_MAP:
                        save_asset_prices(name)
                    mark_updated("spot_asset")
                logger.info("💡 초기 금융 데이터 호출 완료")
            except Exception as e:
                logger.error("🚨 앱 시작 시 데이터 초기화 실패: %s", e)

        threading.Thread(target=run_on_start).start()
