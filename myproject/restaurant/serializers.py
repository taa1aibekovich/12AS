from rest_framework import serializers
from .models import  Product, Extra, Drinks, Location




class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['id', 'name', 'price', 'product', 'description']


class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinks
        fields = ['id', 'name', 'volume', 'price', 'product']




class ProductSerializer(serializers.ModelSerializer):
    extras = ExtraSerializer(many=True, read_only=True)
    drinks = DrinksSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'name', 'description', 'price', 'extras', 'drinks', 'image']



class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['name', 'email', 'address', 'latitude', 'longitude', 'phone']
