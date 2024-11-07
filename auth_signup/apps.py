import os
import json
from django.conf import settings
from django.apps import AppConfig

class AuthSignupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auth_signup'

    def ready(self):
        custom_settings = {
            # 'SOCIALACCOUNT_PROVIDERS': SOCIALACCOUNT_PROVIDERS,
        }
        for setting, value in custom_settings.items():
            if not hasattr(settings, setting):
                setattr(settings, setting, value)
