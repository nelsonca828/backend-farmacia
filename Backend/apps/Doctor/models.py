from django.db import models

# Create your models here.
class Doctor(models.Model):
    nombreDoctor = models.CharField(max_length = 30)
    Apellidos = models.CharField(max_length = 100)
    folioDoctor = models.IntegerField( default = 0)

    def __str__(self):
        return self.nombreDoctor