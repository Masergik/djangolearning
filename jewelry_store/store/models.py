from django.db import models


# Create your models here.
class AbstractCategoryMod(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    vendor_code = models.CharField(max_length=16)
    product_gender = models.SmallIntegerField(default=1)   # продумать таблицу с обозначение женский/мужской
    description = models.TextField()
    metal = models.CharField(max_length=30)
    insertion = models.BooleanField(default=False)
    insert_type = models.CharField(max_length=255)
    size = models.DecimalField(default=0, max_digits=4, decimal_places=1)
    weight = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    product_status = models.BooleanField(default=False)
    product_rating = models.DecimalField(default=0, max_digits=2, decimal_places=0)
    product_price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    date_add = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product_img', null=True)
    collection = models.ForeignKey('store.Collection', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Collection(AbstractCategoryMod):
    image = models.ImageField('image', upload_to='collect_img', null=True, default='', blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


class Category(AbstractCategoryMod):
    image = models.ImageField('image', upload_to='category_img', null=True, default='', blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']


class Store(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.SmallIntegerField(default=0)
    store_address = models.CharField(max_length=255)
    product_name = models.ManyToManyField('store.Product')

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    sale_percent = models.DecimalField(max_digits=3, decimal_places=1)
    collection = models.ForeignKey('store.Collection', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


