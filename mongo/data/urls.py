from django.urls import path, include
from data import views

urlpatterns = [
    path('te/customer/<int:customer_id>/templates', views.tdata, name='tdata'),
]