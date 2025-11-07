from django.urls import path
from inicio.views import inicio, about, crear_colectividad

urlpatterns = [
    path('', inicio),
    path('about/', about),
    path('crear-colectividad/', crear_colectividad),
]
