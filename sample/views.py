from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F, Value, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from store.models import Product, Customer, Collection, Order, OrderItem


def greet(request):

    # writing raw SQL Statement
    products = Product.objects.raw('SELECT * FROM store_product')

    # print(products)
    context = {
        'country': 'Nepal',

    }
    return render(request, 'sample/index.html', context)
