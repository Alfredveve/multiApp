from django.urls import path
from ventes.views import lesVentes



urlpatterns = [
    path('listVente/', lesVentes, name='listVente'),
]
