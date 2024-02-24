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
class VentasListaVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Venta.objects.all().exists():
            venta = Venta.objects.all()

            querySet = venta.order_by('fechaVenta')
            paginador = smallSetPagination()
            results = paginador.paginate_queryset(querySet, request)

            serializador = ListaVentasSerializador2(results, many=True)

            return paginador.get_paginated_response({'Venta' : serializador.data})
        else:
            return Response({'error': 'ningun venta encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Obtener
class VentaVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if Venta.objects.filter(id=id).exists():
            venta = Venta.objects.get(id=id)
            serializador = ListaVentasSerializador2(venta)

            return Response({'Venta': serializador.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun venta encontrado'}, status=status.HTTP_404_NOT_FOUND)
        
    
#Editar
class EditarVentaVista(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        venta = get_object_or_404(Venta, id=id)

        medicamento = data.get('medicamento', None)
        if medicamento is not None:
            venta.medicamento = medicamento

        cantidad = data.get('cantidad', None)
        if cantidad is not None:
            venta.cantidad = cantidad

        fechaVenta = data.get('fechaVenta', None)
        if fechaVenta is not None:
            venta.fechaVenta = fechaVenta

        loteV = data.get('loteV', None)
        if loteV is not None:
            venta.loteV = loteV

        importe = data.get('importe', None)
        if importe is not None:
            venta.importe = importe

        venta.save()

        updated_fields = [key for key in data.keys() if key in [
            'medicamento', 'cantidad', 'fechaVenta', 'loteV', 'importe']]
        return Response({'success': 'Venta editado', 'venta_id': venta.id, 'updated_fields': updated_fields})


#Borrar
class BorrarVentaVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        venta = Venta.objects.get(id=id)
        venta.delete()
        return Response({'success': 'Venta eliminado'})
        

#Crear
class CrearVentaVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializador = VentaSerializador(data=data)

        # Valida los datos
        if serializador.is_valid():
            # Guarda el nuevo animal en la base de datos
            serializador.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Venta creada'}, status=200)

        # Devuelve una respuesta con errores de validación si los datos no son válidos
        return Response(serializador.errors, status=404)

