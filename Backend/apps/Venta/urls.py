from django.urls import path
from .views import *

urlpatterns = [
     #Ventas
    path('Ventas', VentasListaVista.as_view()),  # Listar
    path('Venta/<id>', VentaVista.as_view()),  # Elemento
    path('CrearVenta/', CrearVentaVista.as_view()),  # Crear
    path('EditarVenta/<id>', EditarVentaVista.as_view()),  #Editar
    path('BorrarVenta/<id>', BorrarVentaVista.as_view()) #Borrar

]