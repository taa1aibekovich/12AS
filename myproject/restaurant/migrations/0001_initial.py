# Generated by Django 5.1.2 on 2024-10-27 20:10

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.TimeField()),
                ('longitude', models.TimeField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('telegram', models.URLField()),
                ('instagram', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('product_name_en', models.CharField(max_length=300, null=True)),
                ('product_name_ru', models.CharField(max_length=300, null=True)),
                ('product_name_ky', models.CharField(max_length=300, null=True)),
                ('name', models.CharField(max_length=150)),
                ('name_en', models.CharField(max_length=150, null=True)),
                ('name_ru', models.CharField(max_length=150, null=True)),
                ('name_ky', models.CharField(max_length=150, null=True)),
                ('description', models.TextField()),
                ('description_en', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_ky', models.TextField(null=True)),
                ('price', models.PositiveSmallIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('price', models.PositiveSmallIntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extras', to='restaurant.product')),
            ],
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('volume', models.CharField(max_length=20)),
                ('price', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drinks', to='restaurant.product')),
            ],
        ),
    ]