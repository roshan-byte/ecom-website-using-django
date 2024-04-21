from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status
from .models import Product 
from .serializers import ProductSerializer

@api_view(['GET', 'POST']) # when we add this decorator then the request object become the rest_framework request object.
def product_list(request):
    if request.method == 'GET':
        productQuerySet= Product.objects.all()
        serializer= ProductSerializer(productQuerySet, many=True) # many is True bcz it has to iterate over list of products.
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data) # now it dont need product object it need product data
        # before we access the data we have to validate it first.
        # if serializer.is_valid():
        #     serializer.validated_data # it will return serialize data .
        #     return Response('ok') 
        # else:
        #     return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        print(request.data)
        
        serializer.is_valid(raise_exception=True) # check if the data is vaid or not
        print(serializer.validated_data) # convert the data into object again
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
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
    product = get_object_or_404(Product, pk=id)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serializer.validated_data
        return Response(serializer.data,)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
