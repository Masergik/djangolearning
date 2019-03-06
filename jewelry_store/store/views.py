# from django.db.models import Q
from decimal import Decimal, getcontext
from django.shortcuts import render

from store.models import Product


def product(request, product_id):
    product = Product.objects.get(id=product_id)

    if product.sale_percent.sale_percent != 0:
        price_with_sale = (product.price * (1 - product.sale_percent.sale_percent / Decimal(100))).quantize(Decimal('1.00'))
        print(product.sale_percent.sale_percent, type(product.sale_percent.sale_percent))
    return render(request, 'store/product.html', locals())
