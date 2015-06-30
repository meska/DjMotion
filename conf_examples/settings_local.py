"""
Django settings for djmotion project.

"""

# SECURITY WARNING: keep the secret key used in production secret!
# http://www.miniwebtool.com/django-secret-key-generator/
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djmotion',                      
        'USER': 'postgres',
        'HOST': 'localhost'
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = False


MOTION_REDIS_SERVER = '127.0.0.1'
MOTION_REDIS_CHANNEL = '' 
MOTION_TELEGRAM_PLUGIN = True
MOTION_UPDATE_CAM_SETTINGS = False

# https://core.telegram.org/bots#botfather

TELEGRAM_BOT_TOKEN = ''
TELEGRAM_USE_WEBHOOK = True
TELEGRAM_WEBHOOK_URL = 'http://website.example.com'
