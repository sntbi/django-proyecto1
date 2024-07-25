from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioDeCreacion, EditarPerfil
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra
from django.views.generic.detail import DetailView

def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasena = formulario.cleaned_data.get('password')
            
            user = authenticate (username=usuario, password = contrasena)
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=user)
            
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

@login_required
def editar_perfil(request):
    datosextra = request.user.datosextra
    
    initial_data = {
        'avatar': datosextra.avatar,
        'hobbie': datosextra.hobbie
    }
    
    formulario = EditarPerfil(initial= initial_data, instance=request.user)
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST, request.FILES ,  instance=request.user )
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            hobbie = formulario.cleaned_data.get('hobbie')
            
            if avatar:
                datosextra.avatar = avatar
            else:
                formulario.cleaned_data['avatar'] = datosextra.avatar
                
            datosextra.hobbie = hobbie
            datosextra.save() 
            
            formulario.save()
            return redirect('editar_perfil')
    
    return render (request,'usuarios/editar_perfil.html', {'formulario': formulario})

def aboutme(request):
    return render (request,'usuarios/aboutme.html', {})


class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_pass.html'
    success_url = reverse_lazy('inicio') 
    


@login_required
def ver_perfil(request,id):
    
    datosextra = DatosExtra.objects.get(id=id)
    
    return render (request,'usuarios/ver_perfil.html', {'datosextra':datosextra})