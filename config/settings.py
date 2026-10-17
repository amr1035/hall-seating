import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
DEBUG = os.environ.get("DEBUG", "1") == "1"
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(",")
CSRF_TRUSTED_ORIGINS = [o for o in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",") if o]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")  # خلف بروكسي الاستضافة (https)

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "seating",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": ["django.template.context_processors.request"]},
}]
WSGI_APPLICATION = "config.wsgi.application"
DATABASES = {}          # لا نستخدم قاعدة بيانات: الحفظ في ملف JSON
LANGUAGE_CODE = "ar"
USE_TZ = True
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {"staticfiles": {"BACKEND": "whitenoise.storage.CompressedStaticFilesStorage"}}

# مكان ملف الحفظ (على الاستضافة اجعله على قرص دائم)
DATA_FILE = Path(os.environ.get("DATA_FILE", BASE_DIR / "data.json"))
