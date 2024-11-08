# Django settings for sample project.
import json
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # Add 'postgresql_psycopg2', 'postgresql',
        # 'mysql', 'sqlite3' or 'oracle'.
        "NAME": str(BASE_DIR) + '/db/au_sample.db',
    }
}

TIME_ZONE = "America/Chicago"

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("ar", "Arabic"),
    ("az", "Azerbaijani"),
    ("bg", "Bulgarian"),
    ("ca", "Catalan"),
    ("cs", "Czech"),
    ("da", "Danish"),
    ("de", "German"),
    ("el", "Greek"),
    ("en", "English"),
    ("es", "Spanish"),
    ("et", "Estonian"),
    ("eu", "Basque"),
    ("fa", "Persian"),
    ("fi", "Finnish"),
    ("fr", "French"),
    ("he", "Hebrew"),
    ("hr", "Croatian"),
    ("hu", "Hungarian"),
    ("id", "Indonesian"),
    ("it", "Italian"),
    ("ja", "Japanese"),
    ("ka", "Georgian"),
    ("ko", "Korean"),
    ("ky", "Kyrgyz"),
    ("lt", "Lithuanian"),
    ("lv", "Latvian"),
    ("mn", "Mongolian"),
    ("nb", "Norwegian Bokmål"),
    ("nl", "Dutch"),
    ("pl", "Polish"),
    ("pt-BR", "Portuguese (Brazil)"),
    ("pt-PT", "Portuguese (Portugal)"),
    ("ro", "Romanian"),
    ("ru", "Russian"),
    ("sk", "Slovak"),
    ("sl", "Slovenian"),
    ("sr", "Serbian"),
    ("sr-Latn", "Serbian (Latin)"),
    ("sv", "Swedish"),
    ("th", "Thai"),
    ("tr", "Turkish"),
    ("uk", "Ukrainian"),
    ("zh-hans", "Chinese (Simplified)"),
    ("zh-hant", "Chinese (Traditional)"),
]

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

MEDIA_ROOT = ""

MEDIA_URL = ""

STATIC_ROOT = ""

STATIC_URL = "/static/"

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = "t8_)kj3v!au0!_i56#gre**mkg0&z1df%3bw(#5^#^5e_64!$_"

# List of callables that know how to import templates from various sources.
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

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "allauth.account.middleware.AccountMiddleware",
)

AUTHENTICATION_BACKENDS = ("allauth.account.auth_backends.AuthenticationBackend",)

ROOT_URLCONF = "core.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
    'initsql',
    "auth_signup",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.mfa"
]

USE_TZ = True

AUTH_PASSWORD_VALIDATORS = [{
    "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    "OPTIONS": {
        "min_length": 9,
    },
}]

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

MFA_PASSKEY_LOGIN_ENABLED = True
MFA_PASSKEY_SIGNUP_ENABLED = True
MFA_SUPPORTED_TYPES = ["webauthn", "totp", "recovery_codes",]
ACCOUNT_LOGIN_BY_CODE_ENABLED = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SOCIALACCOUNT_PROVIDERS = {}

def read_social_apps_credentials():
    config_path = str(BASE_DIR) + '/config.json'
    try:
        if not os.path.exists(config_path):
            print('\nNo file found => ' + config_path)
            return {}
        with open(config_path, 'r') as site_config:
            config_info = json.load(site_config)
            social_auth_cred = config_info.get('social_auth')
            return social_auth_cred
    except:
        print('\nError in reading ' + config_path)
        return {}

def add_social_provider_apps():
    provider_candidates = {
        "amazon": {
            "SCOPE": ["profile"],
        },
        "apple": {
            "SCOPE": ["email", "name"],
        },
        "atlassian": {
            "SCOPE": ["read:jira-user"],
        },
        "baidu": {
            "SCOPE": ["basic"],
        },
        "bitbucket_oauth2": {
            "SCOPE": ["account"],
        },
        "dropbox": {
            "SCOPE": ["account_info.read"],
        },
        "dingtalk": {
            "SCOPE": ["user"],
        },
        "edx": {
            "SCOPE": ["email", "profile"],
        },
        "evernote": {
            "SCOPE": ["basic", "notes"],
        },
        "facebook": {
            "SCOPE": ["public_profile"],
            "FIELDS": [
                "id", "email", "name", "first_name", "last_name", "verified", "locale",
                "gender", "link", "picture.type(large)"
            ],
        },
        "figma": {
            "SCOPE": ["file_read"],
        },
        "flickr": {
            "SCOPE": ["read"],
        },
        "github": {
            "SCOPE": ["user", "user:email"],
        },
        "gitlab": {
            "SCOPE": ["read_user"],
        },
        "google": {
            "SCOPE": ["email", "profile"],
            "AUTH_PARAMS": {"access_type": "online"},
        },
        "instagram": {
            "SCOPE": ["user_profile", "user_media"],
        },
        "linkedin_oauth2": {
            "SCOPE": ["r_liteprofile", "r_emailaddress"],
        },
        "microsoft": {
            "SCOPE": ["openid", "email", "profile", "User.Read"],
        },
        "nextcloud": {
            "SCOPE": ["read"],
        },
        "paypal": {
            "SCOPE": ["profile"],
        },
        "pinterest": {
            "SCOPE": ["read_public"],
        },
        "reddit": {
            "SCOPE": ["identity", "read", "submit"],
        },
        "shopify": {
            "SCOPE": ["read_products"],
        },
        "slack": {
            "SCOPE": ["users:read"],
        },
        "snapchat": {
            "SCOPE": ["snaps.read"],
        },
        "soundcloud": {
            "SCOPE": ["non-expiring"],
        },
        "stackexchange": {
            "SCOPE": ["no-expiry"],
        },
        "telegram": {
            "SCOPE": ["user"],
        },
        "tiktok": {
            "SCOPE": ["user.info.basic"],
        },
        "twitter_oauth2": {
            "SCOPE": ["read"],
        },
        "vimeo": {
            "SCOPE": ["public"],
        },
        "weibo": {
            "SCOPE": ["all"],
        },
        "xing": {
            "SCOPE": ["read_profiles"],
        },
    }
    social_auth_cred = read_social_apps_credentials()
    for social_provider in social_auth_cred:
        config_obj = social_auth_cred[social_provider]
        if not provider_candidates.get(social_provider):
            continue
        if not config_obj.get('key') or config_obj.get('key') == 'xx':
            print('No key provided for ' + social_provider)
            continue
        provider_candidates[social_provider]['APP'] = {
            "client_id": config_obj['key'],
            "secret": config_obj['secret'],
        }
        SOCIALACCOUNT_PROVIDERS[social_provider] = provider_candidates[social_provider]
        INSTALLED_APPS.append("allauth.socialaccount.providers." + social_provider)

add_social_provider_apps()
INSTALLED_APPS.append("allauth.usersessions")
