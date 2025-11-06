from django.db import models

class Colectividad(models.Model):
    def __init__(self, pais, comida_tipica, baile_tipico):
        self.pais = pais
        self.comida_tipica = comida_tipica
        self.baile_tipico = baile_tipico
