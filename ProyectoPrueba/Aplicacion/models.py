from django.db import models

# Create your models here.

class Avisos(models.Model):
    tituloAviso = models.CharField(max_length= 40)
    contenidoAviso = models.CharField(max_length= 40)
    

 