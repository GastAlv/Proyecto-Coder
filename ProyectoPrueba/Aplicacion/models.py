from django.db import models

# Create your models here.

class Usuario(models.Model):
    usuario = models.CharField(max_length=30)
    password = models.IntegerField(max_length=15)

class Avisos(models.Model):
    tituloAviso = models.CharField(max_length= 40)
    contenidoAviso = models.CharField(max_length= 40)    
    email = models.EmailField()

class PerfilMusico(models.Model):
    tipoMusico = models.CharField(max_length= 40)
    nombre = models.CharField(max_length= 40)
    apellido = models.CharField(max_length= 40)
    pais = models.CharField(max_length=40)
    estilo = models.CharField(max_length= 40)

