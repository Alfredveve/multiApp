from django.urls import path
from fournisseurs.views import fournisseur



urlpatterns = [
    path('listFournisseur/', fournisseur, name='listFournisseur'),
]
