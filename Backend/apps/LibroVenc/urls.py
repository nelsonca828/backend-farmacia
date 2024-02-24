from django.urls import path
from .views import *

urlpatterns = [
     #Libro
    path('Libros', LibroListaVista.as_view()),  # Listar
    path('Libro/<id>', LibroVista.as_view()),  # Elemento
    path('EditarLibro/<id>', EditarLibroVencVista.as_view()),  # Editar
    path('BorrarLibro/<id>', BorrarLibroVista.as_view()),  # Borrar
    path('CrearLibro', CrearLibroVencVista.as_view()),  # Crear
]