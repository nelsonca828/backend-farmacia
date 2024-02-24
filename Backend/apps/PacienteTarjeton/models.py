from django.db import models

from apps.Medicamento.models import Medicamento

# Create your models here.
class PacienteTarjeton(models.Model):
    nombrePaciente = models.CharField(max_length = 30)
    apellidoPaciente1 = models.CharField(max_length = 30)
    apellidoPaciente2 = models.CharField(max_length = 30) 
    edadPaciente = models.IntegerField
    carnetIdPaciente = models.IntegerField
    enfermedad = models.CharField(max_length = 30) 
    medicamento = models.ForeignKey(Medicamento, on_delete = models.DO_NOTHING)

def __str__(self):
    return self.nombrePaciente