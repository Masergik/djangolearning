from django.contrib import admin
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]


class CollectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Collection._meta.fields]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'collection', 'name', 'created')
    list_filter = ['collection', 'vendor_code']
    search_fields = ('name', )
    inlines = [ProductImageInline]


class SaleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sale._meta.fields]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
