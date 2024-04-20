from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import Product 
from .serializers import ProductSerializer

@api_view(['GET']) # when we add this decorator then the request object become the rest_framework request object.
def product_list(request):
    productQuerySet= Product.objects.all()
    serializer= ProductSerializer(productQuerySet, many=True) # many is True bcz it has to iterate over list of products.
    return Response(serializer.data)

@api_view(['GET'])
def product_detail(request,id):
    """
    # by default decial numbers redered as string this is because of defualt setting of django
    # we can override the default setting by defining
    #     REST_FRAMEWORK = {
    #     'COERCE_DECIMAL_TO_STRING':False
    # } 
    """
    # try:
    #     product = Product.objects.get(pk=id)
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    # we can replace above amount of code with this. 
    product = get_list_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
