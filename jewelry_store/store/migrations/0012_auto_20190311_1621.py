# Generated by Django 2.1.5 on 2019-03-11 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20190308_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug_name',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='slug_name',
            field=models.SlugField(null=True),
        ),
    ]
