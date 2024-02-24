from django.urls import path
from .views import *

urlpatterns = [
     #Medicamentos
    path('Medicamentos', MedicamentosListaVista.as_view()),  # Listar
    path('Medicamento/<id>', MedicamentoVista.as_view()),  # Elemento
    path('EditarMedicamento/<id>', EditarMedicamentoVista.as_view()),  # Editar
    path('BorrarMedicamento/<id>', BorrarMedicamentoVista.as_view()),  # Borrar
    path('CrearMedicamento', CrearMedicamentoVista.as_view()),  # Crear
]