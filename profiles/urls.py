from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', myProfile),
    path('register/', register),
    path('do_register/', doRegister)
]
