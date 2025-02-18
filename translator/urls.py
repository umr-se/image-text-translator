from django.contrib import admin
from django.urls import path, include
from .views import process_image

urlpatterns = [
    path('translator/',process_image ,name ='process_image'),  # Include app URLs
]
