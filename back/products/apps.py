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
        from products.utils.update_checker import should_update
        from products.api.fin_api import get_saving_api, get_deposit_api

        def run_on_start():
            if should_update("saving"):
                get_saving_api()
            if should_update("deposit"):
                get_deposit_api()

        threading.Thread(target=run_on_start).start()
