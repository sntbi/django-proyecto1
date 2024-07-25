from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to='imagen', blank=True, null=True)
  
    # anio = models.IntegerField(default=2006)
  
    def __str__(self):
        return f'{self.nombre} {self.apellido}'