from django.contrib import admin
from django.urls import path,include
from .views import home_screen,login_screen

app_name = 'userdata'
urlpatterns = [
    path('', home_screen),
    path('login_screen',login_screen,name='login_screen')
   
]
