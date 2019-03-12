# from django.db.models import Q
from decimal import Decimal, getcontext
from django.shortcuts import render

from .models import Product, ProductImage, Category, Collection


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    # Создать session_key для неавторизированного пользователя
    if not session_key:
        request.session.cycle_key()

    # Расчет цены товара со скидкой
    if product.sale_percent.sale_percent != 0:
        price_with_sale = (product.price * (1 - product.sale_percent.sale_percent / Decimal(100)))\
            .quantize(Decimal('1.00'))
        print(product.sale_percent.sale_percent, type(product.sale_percent.sale_percent))
    return render(request, 'store/product.html', locals())


def category_view(request, category_slug_name):
    category = Category.objects.get(slug_name=category_slug_name)
    products_of_category = ProductImage.objects.filter(is_active=True, is_main_img=True).select_related('product') \
        .select_related('product__sale_percent').filter(product__category=category)
    context = {
        'category': category,
        'products_of_category': products_of_category,
    }
    return render(request, 'store/category.html', context)


def collection_view(request, collection_slug_name):
    collection = Collection.objects.get(slug_name=collection_slug_name)
    products_of_collection = ProductImage.objects.filter(is_active=True, is_main_img=True).select_related('product') \
        .select_related('product__sale_percent').filter(product__collection=collection)
    context = {
        'collection': collection,
        'products_of_collection': products_of_collection,
    }
    return render(request, 'store/collection.html', context)

