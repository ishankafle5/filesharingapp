from django.contrib import admin
from django.urls import path
from users import views
urlpatterns = [
    path('register', views.signup_page), path('login', views.login_page)
]
