from django.urls import re_path
from django.contrib import admin

from .views import (
    UserCreateAPIView,
    UserLoginAPIView
    )

app_name='users-api'
urlpatterns = [
    re_path(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    re_path(r'^register/$', UserCreateAPIView.as_view(), name='register'),
]
