from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='home'),
    path('add-product/', views.addProduct, name='add-product'),
    ]
