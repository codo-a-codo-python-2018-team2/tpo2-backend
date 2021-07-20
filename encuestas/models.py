from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)  # Acabo de crear una tabla que tiene una property que es un var char
    # de 32 caracteres
    dni = models.PositiveIntegerField()
    nombre= models.CharField(max_length=100)
    apellido = models.CharField(max_length=100, null=True)
    fecha_nacimiento= models.DateField(auto_now=True)