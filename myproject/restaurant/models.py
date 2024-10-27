from django.db import models
from phonenumber_field.modelfields import PhoneNumberField





class Product(models.Model):
    product_name = models.CharField(max_length=300)
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

class Extra(models.Model):
    name = models.CharField(max_length=150)
    price = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='extras')
    description = models.TextField(null =True, blank=True)
    def __str__(self):
        return self.name

class Drinks(models.Model):
    name = models.CharField(max_length=150)
    volume = models.CharField(max_length=20)
    price = models.PositiveSmallIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='drinks')

    def __str__(self):
        return self.name


class Image(models.Model):
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True)


class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.TimeField()
    longitude = models.TimeField()
    email = models.EmailField()
    phone = PhoneNumberField()
    telegram = models.URLField()
    instagram = models.URLField()

    def __str__(self):
        return self.name

