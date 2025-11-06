from django.db import models

class Colectividad(models.Model):
    def __init__(self, nombre_titular, pais, capital, comida_tipica, baile_tipico, cantidad_de_participantes, informacion):
        self.nombre_titular = nombre_titular
        self.pais = pais
        self.capital = capital
        self.comida_tipica = comida_tipica
        self.baile_tipico = baile_tipico
        self.cantidad_de_participantes = cantidad_de_participantes
        self.informacion = informacion