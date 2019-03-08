import datetime

from django.db import models


# Create your models here.
from django.utils.timezone import utc


class AbstractCategoryMod(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default='', blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Product(models.Model):
    GENDER_UNISEX = 0
    GENDER_WOMAN = 1
    GENDER_MAN = 2

    GENDER_CHOICES = (
        (GENDER_UNISEX, 'унисекс'),
        (GENDER_WOMAN, 'женщине'),
        (GENDER_MAN, 'мужчине'),
    )

    name = models.CharField(max_length=30)
    vendor_code = models.CharField(max_length=16)
    gender_for = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=GENDER_WOMAN)
    type = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    metal = models.CharField(max_length=30, null=True, blank=True)
    insertion = models.BooleanField(default=False)
    insert_type = models.CharField(max_length=255, null=True, blank=True)
    rating = models.DecimalField(default=0, max_digits=2, decimal_places=0)
    price = models.DecimalField(default=0, max_digits=7, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    collection = models.ForeignKey('store.Collection', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('store.Category', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    sale_percent = models.ForeignKey('store.Sale', on_delete=models.SET_NULL, null=True)
    user_wishlist = models.ManyToManyField('core.MyUser', blank=True)

    def __str__(self):
        return "%s, арт. %s" % (self.name, self.vendor_code)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ['name']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product_img', blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)
    is_main_img = models.BooleanField(default=False)


class Size(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    size = models.CharField(max_length=5, null=True, blank=True)
    weight = models.DecimalField(default=0, max_digits=5, decimal_places=2)


class Collection(AbstractCategoryMod):
    image = models.ImageField('image', upload_to='collect_img', null=True, default='', blank=True)
#    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"

    def __str__(self):
        return self.name


class Category(AbstractCategoryMod):
    image = models.ImageField('image', upload_to='category_img', null=True, default='', blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']

    def __str__(self):
        return self.name


class Sale(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default='', blank=True)
    sale_percent = models.PositiveSmallIntegerField(default=0)
    collection = models.ForeignKey('store.Collection', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


