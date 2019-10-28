#!/usr/bin/env python
"""Script to run tests and configure settings"""
import sys
import os


import django
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings.configure(
    DEBUG=True,
    USE_TZ=True,
    DATABASES={
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "USER": os.getenv("USER"),
            "NAME": os.getenv("NAME"),
            "PORT": os.getenv("PORT"),
            "HOST": os.getenv("HOST"),
            "PASSWORD": os.getenv("PASSWORD"),
        }
    },
    ROOT_URLCONF="app_test.urls",
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "rest_framework",
        "app_test",
        "track_actions",
    ],
    AUTH_USER_MODEL="app_test.Users",
    MIDDLEWARE=[
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "track_actions.requestMiddleware.RequestMiddleware",
    ],
    TEMPLATES=[
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
                ]
            },
        }
    ],
    REST_FRAMEWORK={
        "DEFAULT_AUTHENTICATION_CLASSES": ("app_test.authentication.Authentication",),
        "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
        "PAGE_SIZE": 20,
    },
    SITE_ID=1,
    NOSE_ARGS=["-s"],
)
django.setup()

from django_nose import NoseTestSuiteRunner
