from rest_framework import serializers
from .models import *

#ListaMedicamentos
class ListaMedicamentosSerializador(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = [             
                'nombreMedicamento',
                'grupo',
                'existencia',
                'precio',
                'estado',
        ]
#Medicamento
class MedicamentoSerializador(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = [             
                'nombreMedicamento',
                'grupo',
                'existencia',
                'precio',
                'estado',
        ]
