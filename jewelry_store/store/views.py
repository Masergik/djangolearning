# from django.db.models import Q
from decimal import Decimal, getcontext
from django.shortcuts import render

from store.models import Product


def product(request, product_id):
    getcontext().prec = 2
    product = Product.objects.get(id=product_id)

    if product.sale_percent.sale_percent is not None:
        price_with_sale = product.price * (1 - Decimal(product.sale_percent.sale_percent / 100))
    return render(request, 'store/product.html', locals())
