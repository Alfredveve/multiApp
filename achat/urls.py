from django.urls import path
from achat.views import achat


urlpatterns = [
    path('listAchat/', achat, name='listAchat'),
]
