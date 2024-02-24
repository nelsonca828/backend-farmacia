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
class PacientesListaVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if PacienteTarjeton.objects.all().exists():
            paciente = PacienteTarjeton.objects.all()

            querySet = paciente.order_by('nombrePaciente')
            paginador = smallSetPagination()
            results = paginador.paginate_queryset(querySet, request)

            serializador = ListaPacientesSerializador2(results, many=True)

            return paginador.get_paginated_response({'Paciente' : serializador.data})
        else:
            return Response({'error': 'ningun paciente encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Obtener
class PacienteVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if PacienteTarjeton.objects.filter(id=id).exists():
            paciente = PacienteTarjeton.objects.get(id=id)
            serializador = ListaPacientesSerializador2([paciente])

            return Response({'Paciente': serializador.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun paciente encontrado'}, status=status.HTTP_404_NOT_FOUND)
        

#Editar
class EditarPacienteTarjetonVista(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        pacienteTarjeton = get_object_or_404(PacienteTarjeton, id=id)

        nombrePaciente = data.get('nombrePaciente', None)
        if nombrePaciente is not None:
            pacienteTarjeton.nombrePaciente = nombrePaciente

        ApellidoPaciente1 = data.get('ApellidoPaciente1', None)
        if ApellidoPaciente1 is not None:
            pacienteTarjeton.ApellidoPaciente1 = ApellidoPaciente1

        ApellidoPaciente2 = data.get('ApellidoPaciente2', None)
        if ApellidoPaciente2 is not None:
            pacienteTarjeton.ApellidoPaciente2 = ApellidoPaciente2

        edadPaciente = data.get('edadPaciente', None)
        if edadPaciente is not None:
            pacienteTarjeton.edadPaciente = edadPaciente

        carnetIdPaciente = data.get('carnetIdPaciente', None)
        if carnetIdPaciente is not None:
            pacienteTarjeton.carnetIdPaciente = carnetIdPaciente

        enfermedad = data.get('enfermedad', None)
        if enfermedad is not None:
            pacienteTarjeton.enfermedad = enfermedad

        medicamento = data.get('medicamento', None)
        if medicamento is not None:
            pacienteTarjeton.medicamento = medicamento

        pacienteTarjeton.save()

        updated_fields = [key for key in data.keys() if key in [
            'nombrePaciente', 'ApellidoPaciente1', 'ApellidoPaciente2', 'edadPaciente', 'carnetIdPaciente', 'enfermedad', 'medicamento']]
        return Response({'success': 'PacienteTarjeton editado', 'pacienteTarjeton_id': pacienteTarjeton.id, 'updated_fields': updated_fields})


#Borrar
class BorrarPacienteTarjetonVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        pacienteTarjeton = PacienteTarjeton.objects.get(id=id)
        pacienteTarjeton.delete()
        return Response({'success': 'PacienteTarjeton eliminado'})
        

#Crear
class CrearPacienteTarjetonVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializador = PacienteSerializador(data=data)

        # Valida los datos
        if serializador.is_valid():
            # Guarda el nuevo animal en la base de datos
            serializador.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Doctor creado'}, status=200)

        # Devuelve una respuesta con errores de validación si los datos no son válidos
        return Response(serializador.errors, status=404)
