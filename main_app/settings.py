from os.path import exists
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-5)7nlk&^8s667jz8z3xwagreb@dv-ls5hqizr%3nn@^z3#neq7'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'main_app.urls'

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

WSGI_APPLICATION = 'main_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

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

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

ALLOW_UNICODE_SLUGS = True

import os
import json

my_apps = ['sam_tools', 'initsql', 'sample_app', 'social_django']
INSTALLED_APPS = my_apps + INSTALLED_APPS

PATH_PREFIX = ''
slashed_path = ''
if PATH_PREFIX:
    slashed_path = '/' + PATH_PREFIX
if not slashed_path.endswith('/'):
    slashed_path += '/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

MEDIA_URL = slashed_path + 'media/'
STATIC_URL = slashed_path + 'static/'
AUTH_PASSWORD_VALIDATORS = []

SOCIAL_AUTH_URL_NAMESPACE = 'social'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    # 'social_core.backends.microsoft.MicrosoftOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

config_info = {}
config_path = str(BASE_DIR)+'/config.json'
if exists(config_path):
    with open(config_path, 'r') as site_config:
        config_info = json.load(site_config)


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config_info['auth']['google']['key']
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config_info['auth']['google']['secret']

SOCIAL_AUTH_FACEBOOK_KEY = config_info['auth']['fb']['key']
SOCIAL_AUTH_FACEBOOK_SECRET = config_info['auth']['fb']['secret']

# SOCIAL_AUTH_TWITTER_KEY = 'your-twitter-api-key'
# SOCIAL_AUTH_TWITTER_SECRET = 'your-twitter-api-secret'
#
#
# SOCIAL_AUTH_LINKEDIN_OAUTH2_KEY = 'your-linkedin-client-id'
# SOCIAL_AUTH_LINKEDIN_OAUTH2_SECRET = 'your-linkedin-client-secret'
#
#
# SOCIAL_AUTH_MICROSOFT_KEY = 'your-microsoft-client-id'
# SOCIAL_AUTH_MICROSOFT_SECRET = 'your-microsoft-client-secret'