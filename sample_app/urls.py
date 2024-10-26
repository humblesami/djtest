import ast
import json

from django.urls import path
from django.shortcuts import render
from social_core.pipeline import social_auth

def process_profile_info(extra_data, details, response):
    del_keys = []
    for key in details:
        extra_data[key] = details[key]
    for key in extra_data:
        if key in ['access_token', 'token_type', 'expires', 'expires_in']:
            del_keys.append(key)
    for key in del_keys:
        del extra_data[key]
    for key in response:
        if key in ['name', 'fullname', 'email', 'picture']:
            actual_val = response[key]
            str_val = str(actual_val)
            extra_data[key] = str_val
    if not extra_data.get('name'):
        extra_data['name'] = user.username
    if not extra_data.get('email'):
        extra_data['email'] = ''
    if not extra_data.get('picture'):
        extra_data['picture'] = ''
    try:
        picture_data = ast.literal_eval(extra_data.get('picture'))
        profile_picture_url = picture_data['data']['url']
        extra_data['picture'] = profile_picture_url
    except:
        pass
    if extra_data.get('fullname'):
        if not extra_data.get('name'):
            extra_data['name'] = extra_data['fullname']
            del extra_data['fullname']
    if not extra_data.get('name'):
        if extra_data.get('last_name'):
            extra_data['name'] = ' '.join([extra_data['first_name'], extra_data['last_name']])
        del extra_data['first_name']
        del extra_data['last_name']
    return extra_data

def load_extra_data(backend, details, response, uid, user, *args, **kwargs):
    social = kwargs.get("social") or backend.strategy.storage.user.get_social_auth(
        backend.name, uid
    )
    if social:
        extra_data = backend.extra_data(user, uid, response, details, *args, **kwargs)
        extra_data = process_profile_info(extra_data, details, response)
        social.set_extra_data(extra_data)

social_auth.load_extra_data = load_extra_data

def hello(request):
    user_info = {
        'name': 'Private',
        'email': 'Private',
        'picture': 'https://www.htgtrading.co.uk/wp-content/uploads/2016/03/no-user-image-square.jpg',
    }
    if request.user.is_authenticated:
        social_account = request.user.social_auth.filter().first()
        if social_account:
            if social_account.extra_data:
                user_data = social_account.extra_data
                for key in user_data:
                    if user_data[key]:
                        user_info[key] = user_data[key]

    return render(request, 'sample_app/index.html', {
        'user_info': user_info,
        'page': 'Home Page'
    })

def about(request):
    return render(request, 'sample_app/index.html', {'page': 'About Use'})


urlpatterns = [
    path('about', about),
    path('', hello),
]
