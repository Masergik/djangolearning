from django.http import JsonResponse
from django.shortcuts import render
from core.models import MyUser
from .forms import CheckoutClientForm
from .models import ProductInCart, Cart


def cart_adding_view(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    new_product, created = ProductInCart.objects.get_or_create(
        session_key=session_key, product_id=product_id, is_active=True, defaults={"quantity": quantity}
    )
    if not created:
        new_product.quantity += int(quantity)
        new_product.save(force_update=True)

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_quantity = products_in_cart.count()
    return_dict["products_total_quantity"] = products_total_quantity

    return_dict["products"] = list()
    for item in products_in_cart:
        product_dict = dict()
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["quantity"] = item.quantity
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def cart_view(request):
    cart = Cart.objects.all()
    context = {
        'cart': cart
    }
    return render(request, 'cart.html', context)


# def add_to_cart_view(request):
#     session_key = request.session.session_key
#     data = request.POST
#     product_id = data.get("product_id")
#     quantity = data.get("quantity")
#
#     new_product, created = ProductInCart.objects.get_or_create(
#         session_key=session_key, product_id=product_id, is_active=True, defaults={"quantity": quantity}
#     )
#     if not created:
#         new_product.quantity += int(quantity)
#         new_product.save(force_update=True)
#
#     products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
#     products_total_quantity = products_in_cart.count()


def checkout_view(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    form = CheckoutClientForm(request.POST)
    if request.user.is_authenticated:
        client = request.user
    cart_total_price = 0
    for product_in_cart in products_in_cart:
        cart_total_price += product_in_cart.total_price
    if request.POST:
        if form.is_valid():
            data = request.POST
            first_name = data.get['first_name']
            last_name = data.get['last_name']
            username = data.get['username']
            email = data.get['email']
            phone = data.get['phone']
            address = data.get['address']

            for name, value in data.items:
                if name.startswith("product_in_cart_"):
                    product_in_cart_id = name.split("product_in_cart_")[1]

        else:
            print('no')
    return render(request, 'order/checkout.html', locals())

