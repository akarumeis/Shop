from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('registration/', show_reg_form, name='reg_form'),
    path('', show_log_form, name='log_form'),
    path('shop/', show_shop, name='shop'),
]