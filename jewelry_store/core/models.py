from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ImageBox(models.Model):
    image_box = models.ImageField(upload_to='all_images')

    object_id = models.IntegerField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    obj = GenericForeignKey()


class MyUser(AbstractUser):
    phone = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    wishlist = models.ManyToManyField('store.Product', blank=True)

    def __str__(self):
        return self.username

