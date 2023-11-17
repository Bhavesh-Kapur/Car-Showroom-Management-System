
from django.contrib import admin
from django.urls import path
from carshowroom import views

urlpatterns = [
    path('', views.about, name='about'),
    path('admindashboard', views.admindashboard, name='admindashboard'),
    path('addcar', views.addcar, name='addcar'),
    path('viewinventory', views.viewinventory, name='viewinventory'),
    path('addcustomer', views.addcustomer, name='addcustomer'),
    path('manageorders', views.manageorders, name='manageorders'),
    path('about', views.about, name='about'),
    path('catalogue', views.catalogue, name='catalogue'),
    path('featured', views.featured, name='featured'),
    path('contact', views.contact, name='contact'),
]
