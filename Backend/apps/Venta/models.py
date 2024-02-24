from django.utils import timezone
from django.db import models
from apps.Medicamento.models import Medicamento
from apps.LibroVenc.models import LibroVenc


# Create your models here.
class Venta(models.Model):
    medicamento = models.ForeignKey(Medicamento, on_delete = models.PROTECT, null = True)
    cantidad = models.IntegerField(default = 0)
    fechaVenta = models.DateField(default=timezone.now)
    loteV = models.ForeignKey(LibroVenc, on_delete = models.PROTECT, null = True)
    importe = models.FloatField(default = 0)


    def save(self, *args, **kargs ):
        #Actualiza la existencia del medicamento al crear una venta
        self.medicamento.existencia -= self.cantidad
        
        #Calcula el importe
        self.importe = self.cantidad * self.medicamento.precio
        
        #Actualiza la cantidad restante del lote
        self.loteV.cantidadRestante -= self.cantidad

        #Cambia el estado a agotado si llega a cero
        if self.medicamento.existencia <= 0:
            self.medicamento.estado = 'ago'
        
        self.medicamento.save()
        self.loteV.save()
        super().save(*args, **kargs)

    def __str__(self):
        return f"{self.medicamento}-{self.fechaVenta}"