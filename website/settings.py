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
SECRET_KEY = os.environ.get("SECRET_KEY", "dummy-secret")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "alexandjennatravels.herokuapp.com",
    "www.jandatravels.com",
    "jandatravels.com",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary_storage",
    "cloudinary",
    "constance",
    "constance.backends.database",
    "website.api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
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
                "django.template.context_processors.media",
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


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = []


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": (
                "%(asctime)s [%(process)d] [%(levelname)s] "
                + "pathname=%(pathname)s lineno=%(lineno)s "
                + "funcname=%(funcName)s %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "null": {"level": "DEBUG", "class": "logging.NullHandler",},
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {"testlogger": {"handlers": ["console"], "level": "INFO",}},
}

DEBUG_PROPAGATE_EXCEPTIONS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
STATICFILES_DIRS = (os.path.join(PROJECT_DIR, "live-static", "static-root"),)

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.environ.get("CLOUD_NAME"),
    "API_KEY": os.environ.get("CLOUD_API_KEY"),
    "API_SECRET": os.environ.get("CLOUD_API_SECRET"),
}

import dj_database_url

prod_db = dj_database_url.config(conn_max_age=500)
DATABASES["default"].update(prod_db)

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
