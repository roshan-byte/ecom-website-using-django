from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.db.models import Q
from django.db.models import F

def say_hello(request):
    # queryset = Product.objects.all()
    # for product in queryset:
    #     print(product)
    # query set using lazy evaluation.
    # every objects return object called manager which is interface to the database.
    # we have bunch of method on query set like "all" that will return query set.

    # list(queryset)
    # queryset[2:7]
    #look up type .
    # in filter function we cant use logical operator. so we have to use lookup type.
    # product = Product.objects.all() #it will return query set.

    # display all the products whose unit price is greater than 60 .
    # display all the products whose unit price is less that 30 
    # product = Product.objects.filter(unit_price__lt=60)

    product = Product.objects.filter(Q(unit_price__gt=70) & Q(title__startswith='Q'))

    return render(request, 'hello.html', {'product': product})


