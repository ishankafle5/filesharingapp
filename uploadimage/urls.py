
from django.contrib import admin
from django.urls import path
from uploadimage import views
urlpatterns = [
    path('uploadpage', views.upload_page),
    path('upload', views.upload_file),
    path('media', views.return_image)

]
