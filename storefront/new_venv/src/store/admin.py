from django.contrib import admin
from store.models import Cart, Customer, Product

admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Product)
