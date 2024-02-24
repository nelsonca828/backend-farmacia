from rest_framework import serializers
from .models import *

#ListaUsuarios
class ListaUsuariosSerializador(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [             
            'nombreUsuario',
            'apellidoUsuario1',
            'apellidoUsuario2',
            'usuario',
            'contraseña',
            'rol',
        ]
#Usuario
class UsuarioSerializador(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [             
           'nombreUsuario',
           'apellidoUsuario1',
           'apellidoUsuario2',
           'usuario',
           'contraseña',
           'rol',
        ]
