from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


class AbstractDeliveryPayMod(models.Model):
    method = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.method


class OrderStatus(models.Model):
    status_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    status = models.ForeignKey('order.OrderStatus', on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    customer_email = models.EmailField(default=None, null=True, blank=True)
    employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
                                 null=True, related_name='employee')
    is_active = models.BooleanField(default=True)
    order_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(max_length=20, default=None, null=True, blank=True)
    customer_lastname = models.CharField(max_length=20, default=None, null=True, blank=True)
    customer_phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    customer_address = models.CharField(max_length=255, default=None, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    delivery_method = models.ForeignKey('order.Delivery', on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey('order.Payment', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Order %s" % self.id

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInCart(models.Model):
    session_key = models.CharField(max_length=255, null=True)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, null=True, default=None, blank=True)
    product = models.ForeignKey('store.Product', on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = int(self.quantity) * self.price_per_item

        super().save(*args, **kwargs)


class Cart(models.Model):
    is_active = models.BooleanField(default=True)
    status = models.ForeignKey('order.OrderStatus', on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField('order.ProductInCart', blank=True)
    cart_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    client_email = models.EmailField(default=None, null=True, blank=True)
    client_firstname = models.CharField(max_length=20, default=None, null=True, blank=True)
    client_lastname = models.CharField(max_length=20, default=None, null=True, blank=True)
    client_phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    client_address = models.CharField(max_length=255, default=None, null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    delivery_method = models.ForeignKey('order.Delivery', on_delete=models.SET_NULL, null=True)
    payment_method = models.ForeignKey('order.Payment', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.id)


class ProductInOrder(models.Model):
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE, null=True, default=None, blank=True)
    product = models.ForeignKey('store.Product', on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    is_active = models.BooleanField(default=True)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return '%s' % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.quantity * self.price_per_item

        super().save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    all_products_in_order = ProductInOrder.objects.filter(order=instance.order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(product_in_order_post_save, sender=ProductInOrder)


class Store(models.Model):
    name = models.CharField(max_length=30)
    store_address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Delivery(AbstractDeliveryPayMod):
    pass


class Payment(AbstractDeliveryPayMod):
    pass
