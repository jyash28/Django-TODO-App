from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse


def home(request):
    print("hello")
    return HttpResponse("hello world")           

urlpatterns = [
    path('',home)
]