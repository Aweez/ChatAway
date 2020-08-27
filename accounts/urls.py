from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('chathome/', views.chatHome, name="chathome"),
    path('logout/', views.logoutUser, name="logout"),
    path('aboutus/', views.aboutUs, name="aboutus"),
    
]