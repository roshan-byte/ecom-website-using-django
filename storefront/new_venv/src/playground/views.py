from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product

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

    return render(request, 'hello.html', {'name': 'Roshan'})


