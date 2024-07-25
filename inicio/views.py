from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Alumno

from inicio.forms import CrearAlumnoFormulario, BuscarAlumno, EditarAlumnoFormulario

import random

from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'inicio/index.html')

# def crear_alumno(request, nombre, apellido):
#     alumno = Alumno(nombre=nombre, apellido=apellido)
#     alumno.save()
#     return render(request,'alumno_templates/creacion.html', {'alumno': alumno})
    
# @login_required  
# def crear_alumno_v2 (request):
#     # V1
#     # print('Valor de la request: ' , request)
#     # print('Valor de GET: ' , request.GET)
#     # print('Valor de POST: ' , request.POST)
    
 
#     # if request.method == 'POST' :
#     #     alumno = Alumno(nombre=request.POST.get('nombre'), apellido=request.POST.get('apellido'))
#     #     alumno.save()
    
#     #V2
#     print('Valor de la request: ' , request)
#     print('Valor de GET: ' , request.GET)
#     print('Valor de POST: ' , request.POST)
    
 
    if request.method == 'POST' :
        formulario = CrearAlumnoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            alumno = Alumno(nombre=datos.get('nombre'), apellido=datos.get('apellido'))
            alumno.save()
            return redirect('alumnos')
            
    formulario = CrearAlumnoFormulario()
    return render (request, 'inicio/crear_alumno_v2.html', {'formulario': formulario})

def crear_alumno(request):
    if request.method == 'POST':
        formulario = CrearAlumnoFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            alumno = Alumno(
                nombre=datos.get('nombre'),
                apellido=datos.get('apellido'),
                imagen=datos.get('imagen') if 'imagen' in request.FILES else None
            )
            alumno.save()
            return redirect('inicio')
    else:
        formulario = CrearAlumnoFormulario()
    return render(request, 'inicio/crear_alumno.html', {'formulario': formulario})


def alumnos(request):
    
    formulario = BuscarAlumno(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
    
    # alumnos = Alumno.objects.all()
    
    return render(request, 'inicio/alumnos.html', {'alumnos': alumnos, 'formulario': formulario})

@login_required
def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect ('alumnos')

@login_required
def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    
    formulario = EditarAlumnoFormulario(initial={'nombre': alumno.nombre , 'apellido' : alumno.apellido })
    
    if request.method == 'POST':
        formulario = EditarAlumnoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            imagen = formulario.cleaned_data.get('imagen')
            
            
            alumno.nombre = info['nombre']
            alumno.apellido = info['apellido']
            alumno.imagen = info['imagen']
            
            alumno.save()
            return redirect ('alumnos')
            
    
    return render (request, 'inicio/editar_alumno.html', {'formulario': formulario, 'alumno': alumno})


# def editar_alumno(request, id):
#     alumno = Alumno.objects.get(id=id)
#     if request.method == 'POST':
#         formulario = EditarAlumnoFormulario(request.POST, request.FILES)
#         if formulario.is_valid():
#             datos = formulario.cleaned_data
#             alumno.nombre = datos.get('nombre')
#             alumno.apellido = datos.get('apellido')

#             if 'imagen' in request.FILES:
#                 alumno.imagen = datos.get('imagen')
#             alumno.save()
#             return redirect('inicio')
#     else:
#         formulario = EditarAlumnoFormulario(initial={
#             'nombre' : alumno.nombre ,
#             'apellido' : alumno.apellido ,
#             'imagen' : alumno.imagen
#         })
        
#         return render(request, 'inicio/editar_alumno.html' , {'formulario' : formulario, 'alumno' : alumno})




# def editar_alumno(request):
    
#     formulario = EditarAlumnoFormulario(instance = request.alumno)
    
#     if request.method == 'POST':
#         formulario= EditarAlumnoFormulario(request.POST, instance=request.user)
#         if formulario.is_valid():
            
            
#             request.alumno.imagen = formulario.cleaned_data.get('imagen')
#             request.alumno.save()
            
#             formulario.save()
#             return redirect('editar_alumno')
            




def ver_alumno (request, id):
    alumno = Alumno.objects.get(id=id)
    return render (request, 'inicio/ver_alumno.html', {'alumno': alumno})


# ESTE ES LA VERSION ORIGINAL
'''
@login_required 
def editar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    
    formulario = EditarAlumnoFormulario(initial={'nombre': alumno.nombre , 'apellido' : alumno.apellido, 'anio': 2002})
    
    if request.method == 'POST':
        formulario = EditarAlumnoFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            alumno.nombre = info['nombre']
            alumno.apellido = info['apellido']
            
            alumno.save()
            return redirect ('alumnos')
            
    
    return render (request, 'inicio/editar_alumno.html', {'formulario': formulario, 'alumno': alumno})
'''

