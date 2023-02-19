"""
Django settings for blango project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import dj_database_url
from pathlib import Path
from configurations import Configuration, values


class Dev(Configuration):

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-+sn%dpa!086+g+%44z9*^j^q-u4n!j(#wl)x9a%_1op@zz2+1-'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue(
        ["localhost", "0.0.0.0", ".codio.io", "127.0.0.1"])
    # X_FRAME_OPTIONS = 'ALLOW-FROM ' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io'
    # CSRF_COOKIE_SAMESITE = None
    # CSRF_TRUSTED_ORIGINS = ['https://' + os.environ.get('CODIO_HOSTNAME') + '-8000.codio.io']
    # CSRF_COOKIE_SECURE = True
    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SAMESITE = 'None'
    # SESSION_COOKIE_SAMESITE = 'None'

    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        "django.contrib.sites",
        'django.contrib.messages',
        'django.contrib.staticfiles',
        "blog",
        "crispy_bootstrap5",
        "crispy_forms",
        "debug_toolbar",
        "blango_auth",
        "allauth",
        "allauth.account",
        "allauth.socialaccount",
        "allauth.socialaccount.providers.google",
        "rest_framework",
        "rest_framework.authtoken"
    ]
    SITE_ID = 1
    ACCOUNT_USER_MODEL_USERNAME_FIELD = None
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_USERNAME_REQUIRED = False
    ACCOUNT_AUTHENTICATION_METHOD = "email"

    CRISPY_TEMPLATE_PACK = "bootstrap5"
    CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
    INTERNAL_IPS = ["127.0.0.1"]
    MIDDLEWARE = [
        "debug_toolbar.middleware.DebugToolbarMiddleware",
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        # 'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    AUTH_USER_MODEL = 'blango_auth.User'

    ROOT_URLCONF = 'blango.urls'
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = "aniquekhan004@gmail.com"
    EMAIL_HOST_PASSWORD = "ivaysxwqfxgfcotu"
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587

    ACCOUNT_ACTIVATION_DAYS = 7
    # REGISTRATION_OPEN = False
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [BASE_DIR / 'templates'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    LOGIN_REDIRECT_URL = 'index'
    LOGOUT_REDIRECT_URL = 'login'
    LOGIN_URL = 'login'

    WSGI_APPLICATION = 'blango.wsgi.application'

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES = {
        "default": dj_database_url.config(default=f"sqlite:///{BASE_DIR}/db.sqlite3"),
        "alternative": dj_database_url.config(
            "ALTERNATIVE_DATABASE_URL", default=f"sqlite:///{BASE_DIR}/alternative_db.sqlite3",
        ),
    }
    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "filters": {
            "require_debug_false": {
                "()": "django.utils.log.RequireDebugFalse",
            },
        },
        "formatters": {
            "verbose": {
                "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
                "style": "{",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "verbose",
            },
            "mail_admins": {
                "level": "ERROR",
                "class": "django.utils.log.AdminEmailHandler",
                "filters": ["require_debug_false"],
            },
        },
        "loggers": {
            "django.request": {
                "handlers": ["mail_admins"],
                "level": "ERROR",
                "propagate": True,
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "DEBUG",
        },
    }
    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        # {
        #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        # },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        # },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        # },
        # {
        #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        # },
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL = '/static/'

    # Default primary key field type
    # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    """
    Let's make Blango a bit more secure, by switching to Argon2 for password hashing.
    """
    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

    REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    }


class Prod(Dev):
    DEBUG = True
    SECRET_KEY = values.SecretValue()
