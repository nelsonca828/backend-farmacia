from django.urls import path
from .views import *

urlpatterns = [
    #Doctores
    path('Doctores', DoctoresListaVista.as_view()),  # Listar
    path('Doctor/<id>', DoctorVista.as_view()),  # Elemento
    path('EditarDoctor/<int:id>', EditarDoctorVista.as_view()),  # Editar
    path('BorrarDoctor/<int:id>',BorrarDoctorVista.as_view()),  # Borrar
    path('CrearDoctor', CrearDoctorVista.as_view()),  # Crear
]