from django.db import models

# Create your models here.


class Medicamento(models.Model): 
    class Meta:
        verbose_name = 'Medicamento'
        verbose_name_plural = 'Medicamentos'
    nombreMedicamento = models.CharField(max_length = 30, unique = True)
    grupo = models.CharField(max_length = 30,blank = True, default = "" )
    existencia = models.IntegerField( default = 0)
    precio = models.FloatField(blank = True, default = 0)
    
    ESTADO = [
        ('dis','Disponible'),
        ('ago', 'Agotado'),
        ('def', 'Déficit'),
        ('con', 'Congelado'),
    ]

    estado = models.CharField(max_length = 15, blank = True, default = "dis", choices = ESTADO)
    
    
    def __str__(self):
        return self.nombreMedicamento
