from django.urls import path
from .views import *
urlpatterns = [
     #Usuarios
    path('Usuarios', UsuariosListaVista.as_view()),  # Listar
    path('Usurio/<id>', UsuarioVista.as_view()),  # Elemento
]