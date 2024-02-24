from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length = 20),
    apellidoUsuario1 = models.CharField(max_length = 20),
    apellidoUsuario2 = models.CharField(max_length = 20),
    usuario = models.CharField(max_length = 20),
    contraseña = models.CharField(max_length = 20),
    rol = models.CharField(max_length = 20)

def __str__(self):
    return self.nombreUsuario