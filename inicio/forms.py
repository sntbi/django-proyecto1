from django import forms

class AlumnoFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    imagen = forms.ImageField(required=False)
    
class CrearAlumnoFormulario(AlumnoFormularioBase):
    ... 
    
class EditarAlumnoFormulario(AlumnoFormularioBase):
    imagen = forms.ImageField(required=False)
    
class BuscarAlumno(forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    nombre = forms.CharField(max_length=20, required=False)
    nombre = forms.CharField(max_length=20, required=False)
    
    