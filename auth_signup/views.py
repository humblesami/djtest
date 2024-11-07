from django.views.generic.base import TemplateView
from allauth.account import app_settings
from allauth.account.adapter import get_adapter
from allauth.account.mixins import (
    LogoutFunctionalityMixin,
    NextRedirectMixin,
    _ajax_response,
)
from allauth.core.internal.httpkit import redirect


class LogoutView(NextRedirectMixin, LogoutFunctionalityMixin, TemplateView):
    template_name = "account/logout." + app_settings.TEMPLATE_EXTENSION

    def get(self, *args, **kwargs):
        url = self.get_next_url() or get_adapter(self.request).get_logout_redirect_url(
            self.request
        )
        self.logout()
        response = redirect(url)
        return _ajax_response(self.request, response)

logout = LogoutView.as_view()