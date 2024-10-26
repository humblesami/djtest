import json
from django.urls import path
from django.shortcuts import render
from social_core.backends.oauth import BaseOAuth2
from social_core.exceptions import AuthMissingParameter
from social_core.utils import handle_http_errors, parse_qs


class FaceBookOath2(BaseOAuth2):
    @handle_http_errors
    def auth_complete(self, *args, **kwargs):
        """Completes login process, must return user instance"""
        self.process_error(self.data)
        if not self.data.get("code"):
            raise AuthMissingParameter(self, "code")
        state = self.validate_state()
        key, secret = self.get_key_and_secret()
        params = {
            "client_id": key,
            "redirect_uri": self.get_redirect_uri(state),
            "client_secret": secret,
            "code": self.data["code"],
        }
        try:
            response = self.request(self.access_token_url(), 'POST', params=params)
        except Exception as ex:
            er = ex.response
            err = json.loads(er.text)['error']
            b = 1
            raise Exception(err)
        try:
            response = response.json()
        except ValueError:
            response = parse_qs(response.text)
        access_token = response["access_token"]
        return self.do_auth(access_token, response, *args, **kwargs)

# social_core.backends.facebook.FacebookOAuth2.auth_complete = FaceBookOath2.auth_complete

def hello(request):
    profile_picture = None
    if request.user.is_authenticated:
        social_account = request.user.social_auth.filter(provider='google-oauth2').first()
        if social_account:
            profile_picture = social_account.extra_data.get('picture')

    return render(request, 'sample_app/index.html', {
        'profile_picture': profile_picture,
        'page': 'Home Page'
    })

def about(request):
    return render(request, 'sample_app/index.html', {'page': 'About Use'})


urlpatterns = [
    path('about', about),
    path('', hello),
]
