from django.contrib import admin
from django.urls import path, re_path
from .views import *

urlpatterns = [
    re_path(r'^generate/(?P<case_id>\d+)/', generate),
    path('do_generate/', doGenerate),
    re_path(r'^delete/(?P<id>\d+)/', delete),
    path('pay/', pay),
    path('medicines/', viewMedicine)
]
