from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-y(g2*7o5b97#$ywih+k8ve-v2+c)b8jonqw+2w0^tt*b=3b-hu'

DEBUG = True

ALLOWED_HOSTS = [' https://www.tech-iitb.org', 'tech-iitb.org','www.tech-iitb.org','localhost']
CSRF_TRUSTED_ORIGINS = ['https://www.tech-iitb.org', 'https://tech-iitb.org']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'config',
    'gunicorn',
    'storages',
]

MIDDLEWARE = [  
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mainwebsite',
        'USER': 'postgres',
        'PASSWORD': 'AMe4kNLwCJdNCo0hWdn6W1tdcSykixoWfCALXaeVbpnD2J7z1OLIEjruUyqq6xmr',
        'HOST': '82.112.236.232',
        'PORT': '5432',
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

AWS_ACCESS_KEY_ID = 'ZXjMyffTHlcmLZ43nX63'
AWS_SECRET_ACCESS_KEY = 'tcrUkUr9k4BXXhzBebeBmdWEZzn9yPN5eHOM5NCe'
AWS_STORAGE_BUCKET_NAME = 'itcmain'  # E.g., 'media'
AWS_S3_ENDPOINT_URL = 'https://files.tech-iitb.org'  # Your custom MinIO endpoint
AWS_S3_REGION_NAME = 'us-east-1'  # Set a default region (MinIO ignores this but it's required by boto3)
AWS_S3_USE_SSL = True  # Use HTTPS

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',  # Cache media files for 1 day
}

# Media file settings
MEDIA_URL = f'https://files.tech-iitb.org/{AWS_STORAGE_BUCKET_NAME}/'
MEDIA_ROOT = ''

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

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = True

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]
