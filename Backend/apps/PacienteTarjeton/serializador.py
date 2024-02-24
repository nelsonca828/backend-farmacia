from rest_framework import serializers

from apps.Medicamento.serializador import MedicamentoSerializador
from .models import *

#ListaPacientes
class ListaPacientesSerializador(serializers.ModelSerializer):
    class Meta:
        model = PacienteTarjeton
        fields = [             
           'nombrePaciente',
           'apellidoPaciente1',
           'apellidoPaciente2',
           'edadPaciente',
           'carnetIdPaciente',
           'enfermedad',
           'medicamento', 
        ]
#Paciente
class PacienteSerializador(serializers.ModelSerializer):
    class Meta:
        model = PacienteTarjeton
        fields = [             
           'nombrePaciente',
           'apellidoPaciente1',
           'apellidoPaciente2',
           'edadPaciente',
           'carnetIdPaciente',
           'enfermedad',
           'medicamento',
        ]

class ListaPacientesSerializador2(serializers.ModelSerializer):
    medicamento = MedicamentoSerializador(many = True, read_only = True)
    class Meta:
        model = PacienteTarjeton
        fields = [             
           'nombrePaciente',
           'apellidoPaciente1',
           'apellidoPaciente2',
           'edadPaciente',
           'carnetIdPaciente',
           'enfermedad',
           'medicamento', 
        ]

        def to_representation(self, instancia):
            representacion = super().to_representation(instancia)

            representacion['medicamento'] = [medicamento['nombre'] for medicamento in representacion['medicamento']]
            return representacion