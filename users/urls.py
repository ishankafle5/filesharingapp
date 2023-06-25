from django.contrib import admin
from django.urls import path
from users import views
urlpatterns = [
    path('', views.login_page),
    path('register', views.signup_page), path('login', views.login_page),
]
