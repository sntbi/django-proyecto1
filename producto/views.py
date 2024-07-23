from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Zapatilla
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# class Zapatillas(ListView):
#     model = Zapatilla
#     template_name = 'zapatillas/listado_de_zapatillas.html'
#     context_object_name = 'zapatillas'

class ZapatillasView(ListView):
    model = Zapatilla
    template_name = 'zapatillas/listado_de_zapatillas.html'
    context_object_name = 'zapatillas'
    
class CrearZapatilla(LoginRequiredMixin, CreateView):
    model = Zapatilla
    template_name = 'zapatillas/crear_zapatilla.html'
    success_url = reverse_lazy('zapatillas')
    fields = ['marca', 'descripcion', 'fecha']
    
class EditarZapatilla( LoginRequiredMixin, UpdateView):
    model = Zapatilla
    template_name = 'zapatillas/editar_zapatilla.html'
    success_url = reverse_lazy('zapatillas')
    fields = ['marca', 'descripcion', 'fecha']
    
class VerZapatilla(DetailView):
    model = Zapatilla
    template_name = 'zapatillas/ver_zapatilla.html'
    
class EliminarZapatilla(LoginRequiredMixin, DeleteView):
    model = Zapatilla
    template_name = "zapatillas/eliminar_zapatilla.html"
    success_url = reverse_lazy('zapatillas')
