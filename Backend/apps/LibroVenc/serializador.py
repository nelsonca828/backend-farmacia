from rest_framework import serializers
from .models import *

#ListaLibroVenc
class ListaLibroVencSerializador(serializers.ModelSerializer):
    class Meta:
        model = LibroVenc
        fields = [             
            'medicamento',
            'lote',
            'fechavenc',
            'cantidadLote',
            'cantidadRestante',
        ]
#LibroVenc
class LibroVencSerializador(serializers.ModelSerializer):
    class Meta:
        model = LibroVenc
        fields = [             
            'medicamento',
            'lote',
            'fechavenc',
            'cantidadLote',
            'cantidadRestante',
        ]


class ListaLibroVencSerializador2(serializers.ModelSerializer):
    medicamento = serializers.CharField(source = 'medicamento.nombreMedicamento', read_only = True)
    class Meta:
        model = LibroVenc
        fields = [             
            'medicamento',
            'lote',
            'fechavenc',
            'cantidadLote',
            'cantidadRestante',
        ]
