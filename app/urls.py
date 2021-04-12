from django.contrib import admin
from django.urls import path
from app.views import home,login,signup
# from django.http import HttpResponse

urlpatterns = [
    path('',home),
    path('login/',login),
    path('signup/',signup)
]