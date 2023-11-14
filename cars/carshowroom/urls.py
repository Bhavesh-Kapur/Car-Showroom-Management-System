
from django.contrib import admin
from django.urls import path
from carshowroom import views

urlpatterns = [
    path('admindashboard', views.admindashboard, name='admindashboard'),
]