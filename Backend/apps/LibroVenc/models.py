from collections.abc import Iterable
from django.db import models
from apps.Medicamento.models import Medicamento
from django.utils import timezone

# Create your models here.
class LibroVenc(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete = models.PROTECT, null = True)
    lote = models.IntegerField(default = 0, null = True)
    fechavenc = models.DateField(default = timezone.now)
    cantidadLote = models.IntegerField(default = 0)
    cantidadRestante = models.IntegerField(default = 0, blank= True)
    
    def save(self, *args, **kargs):
        #Actualiza la existencia del medicamento
        self.medicamento.existencia += self.cantidadLote

        #Define la cantidad Restante
        self.cantidadRestante = self.cantidadLote

        self.medicamento.save()
        super().save(*args, **kargs)

    def __srt__(self):
        return f"{self.medicamento}-{self.lote}"