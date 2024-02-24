from django.urls import path
from .views import *

urlpatterns = [
     #Doctores
    path('Pacientes', PacientesListaVista.as_view()),  # Listar
    path('Paciente/<id>', PacienteVista.as_view()),  # Elemento
]