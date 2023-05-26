from django.shortcuts import render, redirect
from django.http import HttpResponse
from redeem.forms import *
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
    ridersView = Rider.objects.all()[:5]
    passengersView = Passenger.objects.all()[:5]
    ride_requests = RideRequests.objects.all().order_by('-created_at')[:5]
    total_orders = orders.count()
    riders = Rider.objects.all().count()
    passengers = Passenger.objects.all().count()
    ride_completed = RideRequests.objects.filter(status='ended').count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    sos = Sos.objects.all().count()

    context = {
        'orders': orders,
        'ridersView': ridersView,
        'passengersView': passengersView,
        'ride_requests': ride_requests,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,
        'riders': riders,
        'passengers': passengers,
        'ride_completed': ride_completed,
        'sos': sos

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
def viewSos(request):
    sos = Sos.objects.all().order_by('-created_at')
    context = {
        'sos': sos
    }
    return render(request, 'redeem/sos.html', context)


@login_required(login_url='login')
def createRiderOrder(request):
    form = OrderRiderForm(initial={'user': request.user})
    if request.method == 'POST':
        form = OrderRiderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'redeem/order_form.html', context)


@login_required(login_url='login')
def createPassengerOrder(request):
    form = OrderPassengerForm(initial={'user': request.user})
    if request.method == 'POST':
        form = OrderPassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'redeem/order_form.html', context)


@login_required(login_url='login')
def updateRiderOrder(request, pk):
    order = OrderRider.objects.get(id=pk)
    form = OrderRiderForm(instance=order)
    if request.method == 'POST':
        form = OrderRiderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'redeem/orders.html', context)


@login_required(login_url='login')
def updatePassengerOrder(request, pk):
    order = OrderPassenger.objects.get(id=pk)
    form = OrderPassengerForm(instance=order)
    if request.method == 'POST':
        form = OrderPassengerForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'redeem/orders.html', context)


@login_required(login_url='login')
def deletePassengerOrder(request, pk):
    order = OrderPassenger.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'redeem/orders.html', context)


@login_required(login_url='login')
def deleteRiderOrder(request, pk):
    order = OrderRider.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item': order
    }
    return render(request, 'redeem/orders.html', context)


@login_required(login_url='login')
def viewOrders(request):
    orderRider = OrderRider.objects.all().order_by('-created_at')
    orderPassenger = OrderPassenger.objects.all().order_by('-created_at')
    context = {
        'orderRider': orderRider,
        'orderPassenger': orderPassenger
    }
    return render(request, 'redeem/viewOrders.html', context)


@login_required(login_url='login')
def viewUsers(request):
    passengers = Passenger.objects.all().order_by('id')
    riders = Rider.objects.all().order_by('id')
    bikes = BikeDetails.objects.all()
    context = {
        'passengers': passengers,
        'riders': riders,
        'bikes': bikes
    }
    return render(request, 'redeem/allUsers.html', context)


@login_required(login_url='login')
def viewOrdersOne(request, pk):
    orderRider = OrderRider.objects.get(id=pk)
    orderPassenger = OrderPassenger.objects.get(id=pk)

    context = {
        'orderRider': orderRider,
        'orderPassenger': orderPassenger

    }
    return render(request, 'redeem/viewOrders.html', context)


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
def createRideRequest(request):
    form = RideRequestForm(initial={'user': request.user})
    if request.method == 'POST':
        form = RideRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'redeem/ride_request.html', context)


@login_required(login_url='login')
def readRideRequest(request):
    rideRequest = RideRequests.objects.all().order_by('-created_at')
    context = {
        'rideRequest': rideRequest
    }
    return render(request, 'redeem/ride_request.html', context)


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
