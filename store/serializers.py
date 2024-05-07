
from rest_framework import serializers
from .models import Product
from decimal import Decimal


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price',
                  'price_with_tax', 'description', 'genre']

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=270)
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, source='unit_price')
    # description = serializers.CharField(max_length=500)
    genre = serializers.StringRelatedField(source='collection')

    # custom fields
    price_with_tax = serializers.SerializerMethodField('calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
