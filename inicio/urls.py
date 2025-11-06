from django.urls import path
from inicio.views import inicio, about

urlpatterns = [
    path('', inicio),
    path('about/', about),
]
