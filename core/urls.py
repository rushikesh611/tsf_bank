from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview, name='home'),
    path('transferlist',views.transferlistview, name='transfer_list'),
    path('userView/<str:name>',views.userView, name='userView'),
    path('user/<str:name>/confirmation',views.confirmationView, name='confirmation'),
]