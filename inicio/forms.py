from django import forms

class AlumnoFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    anio = forms.CharField(required=False)
    
class CrearAlumnoFormulario(AlumnoFormularioBase):
    ... 
    
class EditarAlumnoFormulario(AlumnoFormularioBase):
    ...
    
class BuscarAlumno(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    nombre = forms.CharField(max_length=20, required=False)
    nombre = forms.CharField(max_length=20, required=False)
    
    