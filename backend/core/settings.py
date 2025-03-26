import uuid
import environ

from core.ckeditor import BASE_CKEDITOR_5_CONFIGS
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()

ENV_FILE_PATH = BASE_DIR / "development.env"

environ.Env.read_env(env_file=ENV_FILE_PATH)

SECRET_KEY = env('DJANGO_SECRET_KEY', default=str(uuid.uuid4()))

DEBUG = env.bool('DJANGO_DEBUG', default=True)

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS', default=['*'])

LOCAL_APPS = [
    'account.apps.AccountConfig',
]

THIRD_PARTY_APPS = [
    # 'ckeditor',
    # 'django_ckeditor_5',
    # 'mptt',
    # 'nested_admin',
    # 'restframework'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]
INSTALLED_APPS += LOCAL_APPS
INSTALLED_APPS += THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

DB_ENGINE = env("DB_ENGINE", default="sqlite3")

if DB_ENGINE == "postgresql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env('DB_NAME', default='mydatabase'),
            'USER': env('DB_USER', default='myuser'),
            'PASSWORD': env('DB_PASSWORD', default='mypassword'),
            'HOST': env('DB_HOST', default='localhost'),
            'PORT': env('DB_PORT', default='5432'),  # Default port for PostgreSQL
        }
    }
elif DB_ENGINE == "mysql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': env("DB_NAME", default='mydatabase'),
            'USER': env("DB_USER", default='myuser'),
            'PASSWORD': env("DB_PASSWORD", default='mypassword'),
            'HOST': env("DB_HOST", default='localhost'),
            'PORT': env("DB_PORT", default='3306'),  # Default port for MySQL
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Uncomment if using ckeditor
# CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
# CKEDITOR_UPLOAD_PATH = "uploads/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "account.User"

AUTHENTICATION_BACKENDS = [
    'account.backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# Stripe
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY", default="sk_***")
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY", default="pk_***")
STRIPE_WEBHOOK_KEY = env("STRIPE_WEBHOOK_KEY", default="whsec_***")

SERVER_DOMAIN = env("SERVER_DOMAIN", default="http://127.0.0.1:8000")
# eg. react,svelte...etc
FRONTEND_DOMAIN = env("FRONTEND_DOMAIN", default="http://127.0.0.1:8000")

if not DEBUG:
    CACHES = {
        'default': {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            'LOCATION': env("REDIS_HOST"),  # Use the REDIS_HOST environment variable
        }
    }
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        }
    }
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_HOST = env("EMAIL_HOST", default="")
EMAIL_PORT = env("EMAIL_PORT", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_password", default="")

# Uncomment if Using RabbitMQ
RABBITMQ_HOST = env("RABBITMQ_HOST")
RABBITMQ_PORT = env("RABBITMQ_PORT")
RABBITMQ_USER = env("RABBITMQ_USER")
RABBITMQ_PASSWORD = env("RABBITMQ_PASSWORD")
RABBITMQ_QUEUE_NAME = env("RABBITMQ_QUEUE_NAME")
RABBITMQ_VHOST = env("RABBITMQ_VHOST")

CKEDITOR_5_CONFIGS = BASE_CKEDITOR_5_CONFIGS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['file', 'console'],
        'level': 'DEBUG',
    },
}

if not DEBUG:
    LOGGING['handlers'] = {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    }


STATIC_VERSION = "1"
