from django.urls import path
from clients.views import client


urlpatterns = [
    path('listClient/', client, name='listClient'),
]
