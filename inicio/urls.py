from django.urls import path
from inicio.views import inicio, about, crear_colectividad, listar_colectividades

urlpatterns = [
    path('', inicio),
    path('about/', about),
    path('crear-colectividad/<str:nombre>/<str:pais>/', crear_colectividad),
    path('listar-colectividades/', listar_colectividades),
]
