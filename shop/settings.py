import os
from pathlib import Path
import dj_database_url

if os.path.isfile('env.py'):
    import env


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY','')

DEBUG = True

ALLOWED_HOSTS = [
    'p5-ishop-9dcecd21e916.herokuapp.com',
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gunicorn',
    'category',
    'accounts',
    'products',
    'cart',
    'orders',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'category.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_USER_MODEL = 'accounts.Account'

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

# Alert Messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email Verification
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'glenncoding@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD','')

# PayPal
PAYPAL_CLIENT_ID = os.getenv('PAYPAL_CLIENT_ID', '')
PAYPAL_SECRET_KEY = os.getenv('PAYPAL_SECRET_KEY', '')

# ElephantSQL
DATABASE_USER = 'Pgdemrvo'
DATABASE_NAME = 'p5-ishop-9dcecd21e916.herokuapp.com'
DATABASEB_PASSWORD = os.environ.get('DATABASE_PASSWORD','')
DATABASE_URL = os.environ.get('DATABASE_URL','')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Check if in development environment
if 'USE_AWS' in os.environ:
    # AWS Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'p5-ishop-9dcecd21e916.herokuapp.com'
    AWS_S3_REGION_NAME = 'us-east-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Static and media files
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
else:
    # Development settings
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "shop/static"),
    ]

    STATIC_ROOT = BASE_DIR / 'staticfiles'
    MEDIA_ROOT = BASE_DIR / 'media'
