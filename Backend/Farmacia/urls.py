

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    #Administrador
    path('admin/', admin.site.urls),
    #Aplicaciones
    path('Doctor/', include ('apps.Doctor.urls')),
    path('LibroVenc/', include ('apps.LibroVenc.urls')),
    path('Medicamento/', include ('apps.Medicamento.urls')),
    path('PacienteTarjeton/', include ('apps.PacienteTarjeton.urls')),
    path('Usuario/', include ('apps.Usuario.urls')),
    path('Venta/', include ('apps.Venta.urls')),
]
