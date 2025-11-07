from django.db import models

class Colectividad(models.Model):
    nombre = models.CharField(max_length=100)  # Ej: "Colectividad Venezolana"
    pais = models.CharField(max_length=100)    # Ej: "Venezuela"
    comida_tipica = models.CharField(max_length=100)  # Ej: "Arepas, Pabellón Criollo, Hallacas"
    baile_tipico = models.CharField(max_length=100)   # Ej: "Joropo, Salsa"
    descripcion = models.TextField(blank=True, null=True)  # Info adicional

    def __str__(self):
        return self.nombre