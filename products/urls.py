from django.urls import path
from products.views import lesProducts


urlpatterns = [
    path('listProduct/', lesProducts, name='listProduct'),
]
