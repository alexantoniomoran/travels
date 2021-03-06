"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from collections import OrderedDict

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "%fk(5n0og)ho(nduha9)hiy)q5zy-420z5-lrt(y(xx#j!2^_0"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "constance",
    "constance.backends.database",
    "rest_framework",
    "website.api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "website.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "website.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_URL = "/static/"

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")

CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"
CONSTANCE_CONFIG = {
    "GOOGLE_MAP_URL": (
        "https://www.google.com/maps/d/embed?mid=19bC1M0RZ32J2YnZHXuRhU5jsuq-0jUqm&ll=38.471156655541165%2C-95.62352748885215&z=4",
        "Embedded Google Map URL",
    ),
    "DISPLAY_NUMBER": ("9", "Number of photos to display"),
    "EXCLUDE_FILTER": (
        "",
        "Comma separated string of filters to exclude from Photos tab",
    ),
    "LONG_EDGE_FOR_IMAGE_COMPRESSION": (
        "1000",
        "How much to compress image by on the long edge",
    ),
    "THUMBNAIL_HEIGHT": ("350", "Height of photo thumbnail"),
    "THUMBNAIL_WIDTH": ("350", "Width of photo thumbnail"),
}
CONSTANCE_CONFIG_FIELDSETS = OrderedDict(
    [
        ("Google Map", ("GOOGLE_MAP_URL",)),
        (
            "Photo Settings",
            (
                "DISPLAY_NUMBER",
                "EXCLUDE_FILTER",
                "LONG_EDGE_FOR_IMAGE_COMPRESSION",
                "THUMBNAIL_HEIGHT",
                "THUMBNAIL_WIDTH",
            ),
        ),
    ]
)
