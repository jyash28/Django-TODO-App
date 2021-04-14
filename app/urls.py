from django.contrib import admin
from django.urls import path
from app.views import home,login,signup
# from django.http import HttpResponse

urlpatterns = [
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('signup/',signup)
]