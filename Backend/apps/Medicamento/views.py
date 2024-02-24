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
class MedicamentosListaVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Medicamento.objects.all().exists():
            medicamento = Medicamento.objects.all()

            querySet = medicamento.order_by(' nombreMedicamento')
            paginador = smallSetPagination()
            results = paginador.paginate_queryset(querySet, request)

            serializador = ListaMedicamentosSerializador(results, many=True)

            return paginador.get_paginated_response({'Medicamento' : serializador.data})
        else:
            return Response({'error': 'ningun medicamento encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Obtener
class MedicamentoVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if Medicamento.objects.filter(id=id).exists():
            medicamento = Medicamento.objects.get(id=id)
            serializador = MedicamentoSerializador(medicamento)

            return Response({'Medicamento': serializador.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun medicamento encontrado'}, status=status.HTTP_404_NOT_FOUND)
        

#Editar
class EditarMedicamentoVista(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        medicamento = get_object_or_404(Medicamento, id=id)

        nombreMedicamento = data.get('nombreMedicamento', None)
        if nombreMedicamento is not None:
            medicamento.nombreMedicamento = nombreMedicamento

        grupo = data.get('grupo', None)
        if grupo is not None:
            medicamento.grupo = grupo

        existencia = data.get('existencia', None)
        if existencia is not None:
            medicamento.existencia = existencia

        precio = data.get('precio', None)
        if precio is not None:
            medicamento.precio = precio

        estado = data.get('estado', None)
        if estado is not None:
            medicamento.estado = estado


        medicamento.save()

        updated_fields = [key for key in data.keys() if key in [
            'nombreMedicamento', 'grupo', 'existencia', 'precio', 'estado']]
        return Response({'success': 'Medicamento editado', 'medicamento_id': medicamento.id, 'updated_fields': updated_fields})


#Borrar
class BorrarMedicamentoVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        medicamento = Medicamento.objects.get(id=id)
        medicamento.delete()
        return Response({'success': 'Medicamento eliminado'})
        

#Crear
class CrearMedicamentoVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializador = MedicamentoSerializador(data=data)

        # Valida los datos
        if serializador.is_valid():
            # Guarda el nuevo animal en la base de datos
            serializador.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Medicamento creado'}, status=200)

        # Devuelve una respuesta con errores de validación si los datos no son válidos
        return Response(serializador.errors, status=404)
