from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from redeem.models import *
from .serializers import *
from django.shortcuts import render, redirect
from rest_framework import viewsets


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        try:
            user = self.get_object()
            orders = user.order_set.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'}, status=404)


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer

    @action(detail=True, methods=['get'])
    def ride_requests(self, request, pk=None):
        try:
            passenger = self.get_object()
            ride_requests = passenger.ride_requests.all()
            serializer = RideRequestSerializer(ride_requests, many=True)
            return Response(serializer.data)
        except Passenger.DoesNotExist:
            return Response({'error': 'Passenger does not exist'}, status=404)


class RiderViewSet(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer

    @action(detail=True, methods=['get'])
    def ride_requests(self, request, pk=None):
        try:
            rider = self.get_object()
            ride_requests = rider.ride_requests.all()
            serializer = RideRequestSerializer(ride_requests, many=True)
            return Response(serializer.data)
        except Rider.DoesNotExist:
            return Response({'error': 'Rider does not exist'}, status=404)


class RideRequestsViewSet(viewsets.ModelViewSet):
    queryset = RideRequests.objects.all()
    serializer_class = RideRequestSerializer

    @action(detail=True, methods=['get'])
    def ride_details(self, request, pk=None):
        try:
            ride_request = self.get_object()
            # Perform custom logic or retrieve additional data related to the ride request
            # Serialize the data if needed
            serializer = self.get_serializer(ride_request)  # Custom serializer for ride details
            return Response(serializer.data)
        except RideRequests.DoesNotExist:
            return Response({'error': 'Ride request does not exist'}, status=404)


class UserTagViewSet(viewsets.ModelViewSet):
    queryset = UserTag.objects.all()
    serializer_class = UserTagSerializer

    @action(detail=True, methods=['get'])
    def user(self, request, pk=None):
        try:
            user_tag = self.get_object()
            user = user_tag.user
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        except UserTag.DoesNotExist:
            return Response({'error': 'UserTag does not exist'}, status=404)

    @action(detail=True, methods=['get'])
    def tag(self, request, pk=None):
        try:
            user_tag = self.get_object()
            tag = user_tag.tag
            serializer = TagSerializer(tag, many=False)
            return Response(serializer.data)
        except UserTag.DoesNotExist:
            return Response({'error': 'UserTag does not exist'}, status=404)


class RideRequestViewSet(viewsets.ModelViewSet):
    queryset = RideRequests.objects.all()
    serializer_class = RideRequestSerializer


class OrderRiderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['get'])
    def rider(self, request, pk=None):
        try:
            order = self.get_object()
            rider = order.rider
            serializer = RiderSerializer(rider, many=False)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'error': 'Order does not exist'}, status=404)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        try:
            product = self.get_object()
            orders = product.order_set.all()
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({'error': 'Product does not exist'}, status=404)


class OrderPassengerViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=True, methods=['get'])
    def passenger(self, request, pk=None):
        try:
            order = self.get_object()
            passenger = order.passenger
            serializer = PassengerSerializer(passenger, many=False)
            return Response(serializer.data)
        except Order.DoesNotExist:
            return Response({'error': 'Order does not exist'}, status=404)


class BikeDetailsViewSet(viewsets.ModelViewSet):
    queryset = BikeDetails.objects.all()
    serializer_class = BikeDetailsSerializer


class SosViewSet(viewsets.ModelViewSet):
    queryset = Sos.objects.all()
    serializer_class = SosSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# @api_view(['GET'])
# def getData(request):
#     products = Product.objects.all()
#
#     serializer = ProductSerializer(products, many=True)
#     data = {
#         'products': serializer.data
#     }
#     return Response(data)
#
#
# @api_view(['POST'])
# def addProduct(request):
#     serializer = ProductSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#
#     return Response(serializer.data)
#
#
# @api_view(['PUT'])
# def updateProduct(request, pk):
#     data = request.data
#     product = Product.objects.get(id=pk)
#     serializer = ProductSerializer(instance=product, data=data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def deleteProduct(request, pk):
#     product = Product.objects.get(id=pk)
#     product.delete()
#     return Response('Item successfully deleted!')
