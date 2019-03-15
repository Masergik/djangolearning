from django.http import JsonResponse
from django.shortcuts import render

from .forms import CheckoutClientForm
from .models import ProductInCart, ProductInOrder, Order


def cart_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    quantity = data.get("quantity")
    size = data.get("size")

    is_delete = data.get("is_delete")
    if is_delete == 'true':
        ProductInCart.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductInCart.objects.get_or_create(
            session_key=session_key, product_id=product_id, size=size, is_active=True, defaults={"quantity": quantity})
        if not created:
            new_product.quantity += int(quantity)
            new_product.save(force_update=True)

    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    products_total_quantity = products_in_cart.count()
    return_dict["products_total_quantity"] = products_total_quantity
    return_dict["products"] = list()

    for item in products_in_cart:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["size"] = item.size
        product_dict["price_per_item"] = item.price_per_item
        product_dict["quantity"] = item.quantity
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def cart_view(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True)
    print(products_in_cart)
    cart_total_price = 0
    for product_in_cart in products_in_cart:
        cart_total_price += product_in_cart.total_price
    return render(request, 'order/cart.html', locals())


def checkout_view(request):
    session_key = request.session.session_key
    products_in_cart = ProductInCart.objects.filter(session_key=session_key, is_active=True, order__isnull=True)

    form = CheckoutClientForm(request.POST)
    if request.user.is_authenticated:
        client = request.user
    cart_total_price = 0
    for product_in_cart in products_in_cart:
        cart_total_price += product_in_cart.total_price
    if request.POST:
        print(request.POST)
        if form.is_valid():
            print("yes")
            data = request.POST
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            username = data.get('username')
            email = data.get('email')
            phone = data.get('phone')
            address = data.get('address')
            comments = data.get('comments')

            order = Order.objects.create(
                customer=request.user, order_total_price=cart_total_price, customer_name=first_name,
                customer_lastname=last_name, customer_phone=phone, customer_address=address, comments=comments,
                customer_email=email, status_id=1)
            print(order)
            context = {
                'order': order,
            }
            for name, value in data.items():
                if name.startswith("product_in_cart_"):
                    product_in_cart_id = name.split("product_in_cart_")[1]
                    product_in_cart = ProductInCart.objects.get(id=product_in_cart_id)

                    product_in_cart.quantity = value
                    product_in_cart.order = order
                    product_in_cart.save(force_update=True)

                    ProductInOrder.objects.create(product=product_in_cart.product, quantity=product_in_cart.quantity,
                                                  price_per_item=product_in_cart.price_per_item,
                                                  total_price=product_in_cart.total_price,
                                                  order=order)

            return render(request, 'order/order-accepted.html', context)
        else:
            print('no')
    return render(request, 'order/checkout.html', locals())

