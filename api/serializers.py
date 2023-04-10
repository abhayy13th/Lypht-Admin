from rest_framework import serializers
from redeem.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'name', 'price', 'discount', 'description', 'stock'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'


class UserTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTag
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sos
        fields = '__all__'


class BikeDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeDetails
        fields = '__all__'


class RideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideRequests
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
