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
class LibroListaVista(APIView):
    permission_classes = (permissions.AllowAny,)


    def get(self, request, format=None):
        if LibroVenc.objects.all().exists():

            libro = LibroVenc.objects.all()

            querySet = libro.order_by('fechavenc')
            paginador = smallSetPagination()
            results = paginador.paginate_queryset(querySet, request)

            serializador = ListaLibroVencSerializador2(results, many=True)

            return paginador.get_paginated_response({'LibroVenc' : serializador.data})
        else:
            return Response({'error': 'ningun Libro encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Obtener
class LibroVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if LibroVenc.objects.filter(id=id).exists():
            libro = LibroVenc.objects.get(id=id)
            serializador = LibroVencSerializador(libro)

            return Response({'Libro': serializador.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun libro encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
#Editar
class EditarLibroVencVista(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        libroVenc = get_object_or_404(LibroVenc, id=id)

        medicamento = data.get('medicamento', None)
        if medicamento is not None:
            libroVenc.medicamento = medicamento

        lote = data.get('lote', None)
        if lote is not None:
            libroVenc.lote = lote

        fechavenc = data.get('fechavenc', None)
        if fechavenc is not None:
            libroVenc.fechavenc = fechavenc

        cantidadLote = data.get('cantidadLote', None)
        if cantidadLote is not None:
            libroVenc.cantidadLote = cantidadLote

        libroVenc.save()

        updated_fields = [key for key in data.keys() if key in [
            'medicamento', 'lote', 'fechavenc', 'cantidadLote']]
        return Response({'success': 'LibroVenc editado', 'libroVenc_id': libroVenc.id, 'updated_fields': updated_fields})


#Borrar
    class BorrarLibroVencVista(APIView):
        permission_classes = (permissions.AllowAny,)

        def delete(self, request, id, format=None):
            libroVenc = LibroVenc.objects.get(id=id)
            libroVenc.delete()
            return Response({'success': 'LibroVenc eliminado'})
        

#Crear
class CrearLibroVencVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializador = LibroVencSerializador(data=data)

        # Valida los datos
        if serializador.is_valid():
            # Guarda el nuevo animal en la base de datos
            serializador.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Libro creado'}, status=200)

        # Devuelve una respuesta con errores de validación si los datos no son válidos
        return Response(serializador.errors, status=404)

#borrar
class BorrarLibroVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        libroVenc = LibroVenc.objects.get(id=id)
        libroVenc.delete()
        return Response({'success': 'LibroVenc eliminado'})
