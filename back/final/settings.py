from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 환경 변수 설정
env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

# API 키들
FIN_API_KEY = env("FIN_API_KEY")
KAKAO_CLIENT_ID = env("KAKAO_CLIENT_ID")
KAKAO_SECRET = env("KAKAO_SECRET")
GOOGLE_CLIENT_ID = env("GOOGLE_CLIENT_ID")
GOOGLE_SECRET = env("GOOGLE_SECRET")
NAVER_CLIENT_ID = env("NAVER_CLIENT_ID")
NAVER_SECRET = env("NAVER_SECRET")
OPENAI_API_KEY = env("OPENAI_API_KEY")

# 보안 설정
SECRET_KEY = "django-insecure--u4ts=j+yvv_lmwv#tv!!z#afpm^(g=gd-ha+y824$f!!ot-2@"
DEBUG = True
ALLOWED_HOSTS = []

# 앱 등록
INSTALLED_APPS = [
    # 로컬 앱
    "accounts",
    "products",
    "community",
    "ai",
    # 서드파티 라이브러리
    "rest_framework",
    "rest_framework.authtoken",
    "drf_yasg",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.kakao",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.naver",
    "corsheaders",
    # 장고 기본 앱
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
]

# allauth가 요구하는 설정
SITE_ID = 1
SOCIALACCOUNT_ADAPTER = "accounts.adapters.CustomSocialAccountAdapter"

# CORS 설정: 모든 출처 허용 (개발 환경)
CORS_ALLOW_ALL_ORIGINS = True

# 미들웨어 설정
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "corsheaders.middleware.CorsMiddleware",
]

# URL 설정
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

# 데이터베이스 설정 (SQLite 사용)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 비밀번호 검증
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# 국제화
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 정적 파일 설정
STATIC_URL = "static/"

# 기본 기본키 타입
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 사용자 모델
AUTH_USER_MODEL = "accounts.User"

# 로그인/회원가입 설정

ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = [
    "email",
    "name",
    # "nickname",
    "password1",
]

# dj-rest-auth 설정
REST_AUTH_REGISTER_SERIALIZERS = {
    "REGISTER_SERIALIZER": "accounts.serializers.CustomRegisterSerializer"
}

# DRF 기본 인증 방식
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# allauth 경고 무시
SILENCED_SYSTEM_CHECKS = ["account.W001"]
