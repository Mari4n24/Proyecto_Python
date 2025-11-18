from django.urls import path
from inicio.views import inicio, about, crear_colectividad, listar_colectividades

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
    path('crear-colectividad/<str:nombre>/<str:pais>/', crear_colectividad, name='crear_colectividad'),
    path('listar-colectividades/', listar_colectividades, name='listar_colectividades'),
]
