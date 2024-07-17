from django.shortcuts import render, redirect
from datetime import datetime

from django.http import HttpResponse
from django.template import Template, Context, loader

from inicio.models import Alumno

from inicio.forms import CrearAlumnoFormulario, BuscarAlumno, EditarAlumnoFormulario

import random

def inicio(request):
    return render(request, 'inicio/index.html')

def template1(request, nombre, apellido, edad):
    fecha = datetime.now()
    return HttpResponse(f'<h1>Mi Template 1</h2> -- Fecha: {fecha} -- Buenas {nombre} {apellido} {edad}')

def template2(request, nombre, apellido, edad):
    
    archivo_abierto = open(r'C:\Users\santi\OneDrive\Escritorio\clase16\templates\template2.html')
    
    template = Template(archivo_abierto.read())
    
    archivo_abierto.close 
    fecha = datetime.now()
    
    datos = { 
             'fecha': fecha ,
             'nombre':nombre, 
             'apellido':apellido,
             'edad':edad,    
             }
    
    contexto = Context(datos)
    
    template_renderizado = template.render(contexto) 
    
    return HttpResponse (template_renderizado)




def template3(request, nombre, apellido, edad):
    
    template = loader.get_template('template2.html')
    
    fecha = datetime.now()
    
    datos = { 
             'fecha': fecha ,
             'nombre':nombre, 
             'apellido':apellido,
             'edad':edad,    
             }
    
    
    template_renderizado = template.render(datos) 
    
    return HttpResponse (template_renderizado)


def template4(request, nombre, apellido, edad):
    
    fecha = datetime.now()
    
    datos = { 
             'fecha': fecha ,
             'nombre':nombre, 
             'apellido':apellido,
             'edad':edad,    
             }
    
    return render(request, 'template2.html', datos)










def probando(request):
    
    lista = list(range(500))
    
    numeros = random.choices(lista, k=50)
    
    return render(request,'probando_if_for.html', {'numeros': numeros})


def crear_alumno(request, nombre, apellido):
    alumno = Alumno(nombre=nombre, apellido=apellido)
    alumno.save()
    return render(request,'alumno_templates/creacion.html', {'alumno': alumno})
    
    
def crear_alumno_v2 (request):
    # V1
    # print('Valor de la request: ' , request)
    # print('Valor de GET: ' , request.GET)
    # print('Valor de POST: ' , request.POST)
    
 
    # if request.method == 'POST' :
    #     alumno = Alumno(nombre=request.POST.get('nombre'), apellido=request.POST.get('apellido'))
    #     alumno.save()
    
    #V2
    print('Valor de la request: ' , request)
    print('Valor de GET: ' , request.GET)
    print('Valor de POST: ' , request.POST)
    
 
    if request.method == 'POST' :
        formulario = CrearAlumnoFormulario(request.POST)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            alumno = Alumno(nombre=datos.get('nombre'), apellido=datos.get('apellido'))
            alumno.save()
            return redirect('alumnos')
            
    formulario = CrearAlumnoFormulario()
    return render (request, 'inicio/crear_alumno_v2.html', {'formulario': formulario})



def alumnos(request):
    
    formulario = BuscarAlumno(request.GET)
    if formulario.is_valid():
        nombre = formulario.cleaned_data['nombre']
        alumnos = Alumno.objects.filter(nombre__icontains=nombre)
    
    # alumnos = Alumno.objects.all()
    
    return render(request, 'inicio/alumnos.html', {'alumnos': alumnos, 'formulario': formulario})

def eliminar_alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    alumno.delete()
    return redirect ('alumnos')

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

def ver_alumno (request, id):
    alumno = Alumno.objects.get(id=id)
    return render (request, 'inicio/ver_alumno.html', {'alumno': alumno})