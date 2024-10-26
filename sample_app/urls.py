from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

def hello(request):
    return HttpResponse("<h1>Home Page Here</h1>")

urlpatterns = [
    path('', hello),
]
