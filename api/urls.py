from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'riders', views.RiderViewSet)
router.register(r'passengers', views.PassengerViewSet)
router.register(r'ride-requests', views.RideRequestViewSet)
router.register(r'user-tags', views.UserTagViewSet)
router.register(r'bike-details', views.BikeDetailsViewSet)
router.register(r'sos', views.SosViewSet)

urlpatterns = [

    path('', include(router.urls)),
]
