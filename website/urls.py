from django.contrib import admin
from django.urls import path,include
from . import views

# app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('sendNewsletter', views.sendNewsletter, name='sendNewsletter'),
    path('sendContact', views.sendContact, name='sendContact'),

]