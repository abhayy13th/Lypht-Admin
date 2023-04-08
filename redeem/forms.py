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



