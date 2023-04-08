from django.shortcuts import render, redirect
from django.http import HttpResponse
from redeem.forms import OrderForm, CreateUserForm
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from redeem.decorators import unauthenticated_user

from redeem.models import *


# Create your views here.
@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    user = User.objects.all()
    total_users = user.count()
    total_orders = orders.count()
    riders = Rider.objects.all().count()
    passengers = Passenger.objects.all().count()
    ride_completed = RideRequests.objects.filter(status='ended').count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'users': user,
        'total_orders': total_orders,
        'total_users': total_users,
        'delivered': delivered,
        'pending': pending,
        'riders': riders,
        'passengers': passengers,
        'ride_completed': ride_completed

    }
    return render(request, 'redeem/dashboard.html', context)


@login_required(login_url='login')
def products(request):
    Product.objects.all()
    return render(request, 'redeem/products.html', {'products': Product.objects.all()})


@login_required(login_url='login')
def users(request, pk_test):
    user = User.objects.get(id=pk_test)
    orders = user.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'user': user,
        'orders': orders,
        'order_count': order_count,
        'myFilter': myFilter
    }
    return render(request, 'redeem/orders.html', context)


@login_required(login_url='login')
def createOrder(request):
    form = OrderForm(initial={'user': request.user})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'redeem/order_form.html', context)


@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'redeem/order_form.html', context)


@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'redeem/delete.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username/Password is incorrect')

    return render(request, 'redeem/login.html')


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('/login')
    context = {
        'form': form
    }

    return render(request, 'redeem/register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
