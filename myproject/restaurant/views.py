from rest_framework import viewsets
from .models import  Product, Extra, Drinks, Location
from .serializers import (
    ProductSerializer,
    ExtraSerializer,
    DrinksSerializer,
    LocationSerializer
)
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Location




class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ExtraViewSet(viewsets.ModelViewSet):
    queryset = Extra.objects.all()
    serializer_class = ExtraSerializer


class DrinksViewSet(viewsets.ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
