from django.apps import AppConfig
from django.conf import settings


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"

    def ready(self):
        import sys

        if "makemigrations" in sys.argv or "migrate" in sys.argv:
            return

        from allauth.socialaccount.models import SocialApp
        from django.contrib.sites.models import Site

        site = Site.objects.get(id=settings.SITE_ID)

        providers = [
            {
                "provider": "kakao",
                "name": "Kakao",
                "client_id": settings.KAKAO_CLIENT_ID,
                "secret": settings.KAKAO_SECRET,
            },
            {
                "provider": "google",
                "name": "Google",
                "client_id": settings.GOOGLE_CLIENT_ID,
                "secret": settings.GOOGLE_SECRET,
            },
            {
                "provider": "naver",
                "name": "Naver",
                "client_id": settings.NAVER_CLIENT_ID,
                "secret": settings.NAVER_SECRET,
            },
        ]

        for p in providers:
            if not SocialApp.objects.filter(provider=p["provider"]).exists():
                app = SocialApp.objects.create(
                    provider=p["provider"],
                    name=p["name"],
                    client_id=p["client_id"],
                    secret=p["secret"],
                )
                app.sites.add(site)
