from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))
FIN_API_KEY = env("FIN_API_KEY")

KAKAO_CLIENT_ID = env("KAKAO_CLIENT_ID")
KAKAO_SECRET = env("KAKAO_SECRET")

GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID")
GOOGLE_SECRET = env("GOOGLE_SECRET")

NAVER_CLIENT_ID = env("NAVER_CLIENT_ID")
NAVER_SECRET = env("NAVER_SECRET")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure--u4ts=j+yvv_lmwv#tv!!z#afpm^(g=gd-ha+y824$f!!ot-2@"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    # apps
    "accounts",
    "products",
    "community",
    # library
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",  # swagger
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",  # 소셜 로그인
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.naver",
    "corsheaders",
    # ---
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 추가
    "django.contrib.sites",
]
# allauth가 요구
SITE_ID = 1

# 소셜 로그인 어댑터
SOCIALACCOUNT_ADAPTER = "accounts.adapters.CustomSocialAccountAdapter"

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # dj-rest-auth
    "allauth.account.middleware.AccountMiddleware",
    # cors
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "final.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "final.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Custom User Setting
AUTH_USER_MODEL = "accounts.User"

# ACCOUNT_LOGIN_METHODS = {"username"}  # 혹은 {"email"} 또는 {"username", "email"}
# ACCOUNT_SIGNUP_FIELDS = {
#     "username": {"required": True},
#     "email": {"required": True},
#     "nickname": {"required": False},
#     "password1": {"required": True},
#     "password2": {"required": False},
# }
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_EMAIL_REQUIRED = True

# 비밀번호 재설정 이후 자동 로그인
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "accounts.serializers.CustomRegisterSerializer"
}
ACCOUNT_SIGNUP_FIELDS = ["username", "email", "password1", "age"]


# django-allauth 경고 무시
SILENCED_SYSTEM_CHECKS = ["account.W001"]
