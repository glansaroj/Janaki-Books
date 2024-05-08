
from rest_framework import serializers
from .models import Product, Collection
from decimal import Decimal


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'slug', 'unit_price', 'inventory',
                  'price_with_tax', 'description', 'collection', ]

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=270)
    # price = serializers.DecimalField(
    #     max_digits=6, decimal_places=2, source='unit_price')
    # description = serializers.CharField(max_length=500)
    # genre = serializers.StringRelatedField(source='collection')

    # custom fields
    price_with_tax = serializers.SerializerMethodField('calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']

    product_count = serializers.IntegerField(read_only=True)
