from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioDeCreacion


def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasena = formulario.cleaned_data.get('password')
            
            user = authenticate (username=usuario, password = contrasena)
            
            django_login(request, user)
            
            return redirect('inicio')
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def register(request):
    
    formulario = FormularioDeCreacion()
    
    if request.method == 'POST':
        formulario =UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    
    return render(request, 'usuarios/register.html', {'formulario':formulario})