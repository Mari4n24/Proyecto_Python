from django.db import models

class Colectividad(models.Model):
    nombre = models.CharField(max_length=100) 
    pais = models.CharField(max_length=100)    
