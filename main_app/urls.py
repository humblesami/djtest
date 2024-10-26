from django.urls import re_path
from django.conf import settings
from django.contrib import admin
from django.views.static import serve


from django.http import HttpResponse
from django.urls import re_path, path, include
from django.conf import settings
from django.contrib import admin
from django.views.static import serve

urls_prefix = settings.PATH_PREFIX or ''
if urls_prefix:
    urls_prefix += '/'

def media_static_urls():
    media_root = {'document_root': settings.MEDIA_ROOT}
    media_urls = [re_path(r'^' + urls_prefix + 'media/(?P<path>.*)$', serve, media_root)]

    static_root = {'document_root': settings.STATIC_ROOT}
    static_urls = [re_path(r'^' + urls_prefix + 'static/(?P<path>.*)$', serve, static_root)]

    all_urls = media_urls + static_urls
    return all_urls


def home(request):
    return HttpResponse('<h2>Home</h2>')

app_urls = [
    re_path(urls_prefix + 'admin/', admin.site.urls),
    re_path(urls_prefix, include('sample_app.urls')),
]


urlpatterns = media_static_urls() + app_urls
