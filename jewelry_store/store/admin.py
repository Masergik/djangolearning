from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'collection', 'name', 'created')
    list_filter = ['collection', 'vendor_code']
    search_fields = ('name', )
    inlines = [ProductImageInline]


admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale)
