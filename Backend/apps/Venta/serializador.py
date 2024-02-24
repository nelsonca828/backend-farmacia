from rest_framework import serializers
from .models import *

#ListaVentas
class ListaVentasSerializador(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = [             
            'medicamento',
            'cantidad',
            'fechaVenta',
            'loteV',
            'importe',
        ]
#Venta
class VentaSerializador(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = [             
            'medicamento',
            'cantidad',
            'fechaVenta',
            'loteV',
            'importe',
        ]

class ListaVentasSerializador2(serializers.ModelSerializer):
    medicamento = serializers.CharField(source='medicamento.nombreMedicamento', read_only = True )
    loteV = serializers.IntegerField(source= 'loteV.lote', read_only = True)
    class Meta:
        model = Venta
        fields = [             
            'medicamento',
            'cantidad',
            'fechaVenta',
            'loteV',
            'importe',
        ]