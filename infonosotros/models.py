from django.db import models

# Create your models here.
class alumno(models.Model):
    nombre = models.CharField(max_length=40)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80)
    edad = models.IntegerField()
    num_boleta = models.CharField(max_length=10)
    promedio_general = models.FloatField()