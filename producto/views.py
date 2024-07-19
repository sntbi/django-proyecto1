from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Zapatilla
# Create your views here.

# class Zapatillas(ListView):
#     model = Zapatilla
#     template_name = 'zapatillas/listado_de_zapatillas.html'
#     context_object_name = 'zapatillas'

class ZapatillasView(ListView):
    model = Zapatilla
    template_name = 'zapatillas/listado_de_zapatillas.html'
    context_object_name = 'zapatillas'