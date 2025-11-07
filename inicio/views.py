from django.shortcuts import render
from django.http import HttpResponse 
from inicio.models import Colectividad

def inicio(request):
    return render(request, "inicio.html")

def about(request):
    return render(request, "about.html")

def crear_colectividad(request, nombre, pais):
    
    colectividad = Colectividad(nombre=nombre, pais=pais)
    colectividad.save()
    
    return render(request, "crear_colectividad.html", {"objeto_guardado": colectividad})

def listar_colectividades(request):
    
    colectividades = Colectividad.objects.all()
    
    return render(request, "listar_colectividades.html", {'listado_colectividades': colectividades})