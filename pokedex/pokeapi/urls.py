from django.urls import path 
from .views import recebePokemon
from . import views

urlpatterns = [
    path('pokemons/', views.recebePokemon, name='algo'),
    path('', views.recebeForm),
]