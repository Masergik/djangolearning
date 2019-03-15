from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    list_filter = ['status', 'is_active']
    search_fields = ('id', 'client', 'employee')
    inlines = [ProductInOrderInline]


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderStatus._meta.fields]
    list_filter = ['status_name', 'is_active']


class ProductInOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInOrder._meta.fields]


class ProductInCartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductInCart._meta.fields]

    class Meta:
        model = ProductInCart


class CartAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Cart._meta.fields]

    class Meta:
        model = Cart


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)
admin.site.register(ProductInCart, ProductInCartAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Delivery)
admin.site.register(Payment)
admin.site.register(Store)


