from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class ImageBox(models.Model):
    image_box = models.ImageField(upload_to='all_images')

    object_id = models.IntegerField(null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    obj = GenericForeignKey()
