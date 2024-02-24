from rest_framework import serializers
from .models import *

#ListaDoctores
class ListaDoctoresSerializador(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id',
            'nombreDoctor',
            'Apellidos',
            'folioDoctor',
        ]
        
#Doctor
class DoctorSerializador(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id',
            'nombreDoctor',
            'Apellidos',
            'folioDoctor',
        ]
