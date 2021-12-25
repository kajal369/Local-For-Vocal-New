from django.contrib import admin
from django.urls import path,include 
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('ragistration',views.login,name='login'),
    path('home',views.index,name='index'),
    path('index',views.index,name='index'),
]
