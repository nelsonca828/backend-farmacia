import json
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from .serializador import *
from .models import *
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .paginación import *

# Create your views here.
#Listar
class DoctoresListaVista(APIView):
    def get(self, request, format=None):
        if Doctor.objects.all().exists():
            doctor = Doctor.objects.all()

            querySet = doctor.order_by('nombreDoctor')
            paginador = smallSetPagination()
            results = paginador.paginate_queryset(querySet, request)

            serializador = ListaDoctoresSerializador(results, many=True)

            return paginador.get_paginated_response({'Doctor' : serializador.data})
        else:
            return Response({'error': 'ningun doctor encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Obtener
class DoctorVista(APIView):
    def get(self, request, id, format=None):
        if Doctor.objects.filter(id=id).exists():
            doctor = Doctor.objects.get(id=id)
            serializador = DoctorSerializador(doctor)

            return Response({'Doctor': serializador.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun doctor encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Editar
class EditarDoctorVista(APIView):
    # parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id,):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'Error': 'Doctor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DoctorSerializador(doctor,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# data = request.data
# print(data)
# doctor = get_object_or_404(Doctor, id=id)
# print(doctor)
        
# nombreDoctor = data.get('nombreDoctor', None)
# if nombreDoctor is not None:
#     doctor.nombreDoctor = nombreDoctor

# Apellidos = data.get('Apellidos', None)
# if Apellidos is not None:
#     doctor.Apellidos = Apellidos

# folioDoctor = data.get('folioDoctor', None)
# if folioDoctor is not None:
#     doctor.folioDoctor = folioDoctor

# doctor.save()

# updated_fields = [key for key in data.keys() if key in [
#     'nombreDoctor', 'Apellidos', 'folioDoctor']]
# return Response({'success': 'Doctor editado', 'doctor_id': doctor.id, 'updated_fields': updated_fields})
    
#Borrar
class BorrarDoctorVista(APIView):
    def delete(self, request, id, format=None):
        try:
            doctor = Doctor.objects.get(id=id)
        except Doctor.DoesNotExist:
            return Response({'Error': 'Doctor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
        doctor.delete()
        return Response({'success': 'Doctor eliminado'})    

#Crear
class CrearDoctorVista(APIView):
    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializador = DoctorSerializador(data=data)

        # Valida los datos
        if serializador.is_valid():
            # Guarda el nuevo Doctor en la base de datos
            serializador.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Doctor creado'}, status=200)

        # Devuelve una respuesta con errores de validación si los datos no son válidos
        return Response(serializador.errors, status=404)
