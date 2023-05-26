from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('users/', views.viewUsers, name='users'),
    path('users/<str:pk_test>/', views.users, name='orders'),
    path('createOrder/', views.createOrder, name='create_Order'),
    path('updateOrder/<str:pk>/', views.updateOrder, name='update_Order'),
    path('deleteOrder/<str:pk>/', views.deleteOrder, name='delete_Order'),
    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('view-orders/', views.viewOrders, name='view_orders'),
    path('view-ride-requests/', views.readRideRequest, name='view_ride_requests'),
    path('sos/', views.viewSos, name='sos'),


    ]
