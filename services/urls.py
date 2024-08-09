from django.urls import path
from services.views import lesServices


urlpatterns = [
    path('listService/', lesServices, name='listService'),
]
