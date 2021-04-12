from django.contrib import admin
from django.urls import path
from app.views import home
# from django.http import HttpResponse

urlpatterns = [
    path('',home)
]