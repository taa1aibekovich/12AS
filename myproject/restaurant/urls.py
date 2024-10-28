from django.urls import path
from .views import *

urlpatterns = [

    # Product URLs
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product_list'),
    path('<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product_detail'),

    # Extra URLs
    path('extras/', ExtraViewSet.as_view({'get': 'list', 'post': 'create'}), name='extra_list'),
    path('extras/<int:pk>/', ExtraViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='extra_detail'),

    # Drinks URLs
    path('drinks/', DrinksViewSet.as_view({'get': 'list', 'post': 'create'}), name='drink_list'),
    path('drinks/<int:pk>/', DrinksViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='drink_detail'),

    # Location URLs
    path('locations/', LocationViewSet.as_view({'get': 'list', 'post': 'create'}), name='location_list'),
    path('locations/<int:pk>/', LocationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location_detail'),
]
