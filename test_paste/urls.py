from django.template.defaulttags import url
from django.urls import path, re_path
from django.contrib import admin

from .views import index

app_name = "test_paste"

urlpatterns = [
    re_path(r'^(?P<pk>\d+)?$', index, name="index"),
]
