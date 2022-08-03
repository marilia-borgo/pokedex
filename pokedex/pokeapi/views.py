import json
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from requests import get
from django.http import JsonResponse, HttpResponse

def recebePokemon(request):
        nome = request.GET.get('pokemi')
        url = get(f'https://pokeapi.co/api/v2/pokemon/{nome}/')
        d=json.loads(url.content.decode("utf-8"))
        abilities_name = d.get('abilities')[0].get('ability').get('name')
        weigth = d.get('weight')
        foto = d.get('sprites').get('front_default')
        


    
        return render(request, 'pokeapi/main.html', {"url_clara":abilities_name, "peso":weigth, "foto":foto})

def recebeForm(request):
    return render(request, "pokeapi/main.html")

