from .models import Product , Collection
from decimal import Decimal
from rest_framework import serializers 

# serializer convert model instance into python dictionary .
# all field of an object we cant expose.
# that is why we have two type of serializer internal and external.
# external serializer that exposes fields that we are going to show clients.

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source='unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = serializers.PrimaryKeyRelatedField(
        queryset=Collection.objects.all()
    )
    def calculate_tax(self , product: Product):
        return product.unit_price*Decimal(1.1)