from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'