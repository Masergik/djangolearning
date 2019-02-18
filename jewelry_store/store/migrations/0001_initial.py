# Generated by Django 2.1.5 on 2019-02-05 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('vendor_code', models.CharField(max_length=16)),
                ('product_gender', models.IntegerField(max_length=1)),
                ('description', models.TextField()),
                ('metal', models.CharField(max_length=30)),
                ('insertion', models.CharField(max_length=30)),
                ('insert_type', models.CharField(max_length=30)),
                ('size', models.DecimalField(decimal_places=1, max_digits=4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('product_status', models.BooleanField(default=False)),
                ('product_rating', models.DecimalField(decimal_places=0, default=0, max_digits=2)),
                ('product_price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('date_add', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sale_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('sale_percent', models.DecimalField(decimal_places=1, max_digits=3)),
                ('collection', models.ManyToManyField(to='store.Collection')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(max_length=3)),
                ('store_address', models.CharField(max_length=255)),
                ('product_name', models.ManyToManyField(to='store.Product')),
            ],
        ),
    ]
