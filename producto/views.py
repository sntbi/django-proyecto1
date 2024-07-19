from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Zapatilla
from django.urls import reverse_lazy
# Create your views here.

# class Zapatillas(ListView):
#     model = Zapatilla
#     template_name = 'zapatillas/listado_de_zapatillas.html'
#     context_object_name = 'zapatillas'

class ZapatillasView(ListView):
    model = Zapatilla
    template_name = 'zapatillas/listado_de_zapatillas.html'
    context_object_name = 'zapatillas'
    
class CrearZapatilla(CreateView):
    model = Zapatilla
    template_name = 'zapatillas/crear_zapatilla.html'
    success_url = reverse_lazy('zapatillas')
    fields = ['marca', 'descripcion', 'fecha']
    
class EditarZapatilla(UpdateView):
    ...
    
class VerZapatilla(DetailView):
    model = Zapatilla
    template_name = 'zapatillas/ver_zapatilla.html'