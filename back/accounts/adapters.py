import uuid
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
import requests
import json


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)

        extra_data = sociallogin.account.extra_data
        provider = sociallogin.account.provider
        print(extra_data)
        if provider == "kakao":
            kakao_account = extra_data.get("kakao_account", {})
            profile = kakao_account.get("profile", {})

            user.email = kakao_account.get("email", "")
            user.nickname = profile.get("nickname", "")
            user.profile_image = profile.get("profile_image_url", None)
            user.name = profile.get("nickname", "")
            user.age = 0
            user.annual_income = None

        elif provider == "google":
            user.email = extra_data.get("email", "")
            user.nickname = extra_data.get("name", "")
            user.profile_image = extra_data.get("picture", None)
            user.name = extra_data.get("name", "")
            user.age = 0
            user.annual_income = None

        return user

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        user.username = f"user_{uuid.uuid4().hex[:10]}"

        try:
            # DRF Request → .data 사용
            if hasattr(request, "data"):
                data = request.data.get("data", {})
            else:
                # WSGIRequest → request.body 사용
                body = request.body.decode("utf-8")
                parsed = json.loads(body)
                data = parsed.get("data", {})
        except Exception as e:
            data = {}

        profile = data.get("profile", {})
        user.email = data.get("email", user.email or "")
        user.nickname = profile.get("nickname", user.nickname or "")
        user.name = data.get("name", user.name or "")
        user.profile_image = profile.get(
            "profile_image_url", user.profile_image or None
        )

        user.save()
        return user


class KakaoOAuth2Adapter(OAuth2Adapter):
    provider_id = "kakao"
    access_token_url = "https://kauth.kakao.com/oauth/token"
    authorize_url = "https://kauth.kakao.com/oauth/authorize"
    profile_url = "https://kapi.kakao.com/v2/user/me"

    def complete_login(self, request, app, token, **kwargs):
        headers = {"Authorization": f"Bearer {token.token}"}
        resp = requests.get(self.profile_url, headers=headers)
        resp.raise_for_status()
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)


class CustomGoogleOAuth2Adapter(OAuth2Adapter):
    provider_id = "google"
    access_token_url = "https://oauth2.googleapis.com/token"
    authorize_url = "https://accounts.google.com/o/oauth2/v2/auth"
    profile_url = "https://www.googleapis.com/oauth2/v1/userinfo"

    def complete_login(self, request, app, token, **kwargs):
        headers = {"Authorization": f"Bearer {token.token}"}
        response = requests.get(self.profile_url, headers=headers)
        response.raise_for_status()
        extra_data = response.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)
