from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User as UserAuth
from .models import *


#  RedeemCode model make first

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = UserAuth
        fields = ['username', 'email', 'password1', 'password2']


class RiderForm(ModelForm):
    class Meta:
        model = Rider
        fields = '__all__'


class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'


class RideRequestForm(ModelForm):
    class Meta:
        model = RideRequests
        fields = '__all__'


class BikeDetailsForm(ModelForm):
    class Meta:
        model = BikeDetails
        fields = '__all__'


class OrderRiderForm(ModelForm):
    class Meta:
        model = OrderRider
        fields = '__all__'


class OrderPassengerForm(ModelForm):
    class Meta:
        model = OrderPassenger
        fields = '__all__'
