from django.contrib import admin
from store.models import Product, Store, Collection, Category, Sale


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'collection', 'name', 'date_add')
    search_fields = ('name', )


admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product, ProductAdmin)
admin.site.register(Store)
admin.site.register(Sale)
