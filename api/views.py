from rest_framework.response import Response
from rest_framework.decorators import api_view
from redeem.models import *
from .serializers import *


@api_view(['GET'])
def getData(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    data = {
        'products': serializer.data
    }
    return Response(data)


@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


