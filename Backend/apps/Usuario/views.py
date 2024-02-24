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
class UsuariosListaVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        if Usuario.objects.all().exists():
            usuario = Usuario.objects.all()

            querySet = usuario.order_by('nombreUsuario')
            paginador = smallSetPagination()
            results = paginador.paginate_queryset(querySet, request)

            serializador = ListaUsuariosSerializador(results, many=True)

            return paginador.get_paginated_response({'Usuario' : serializador.data})
        else:
            return Response({'error': 'ningun usuario encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Obtener
class UsuarioVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, id, format=None):
        if Usuario.objects.filter(id=id).exists():
            usuario = Usuario.objects.get(id=id)
            serializador = UsuarioSerializador(usuario)

            return Response({'Usuario': serializador.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'ningun usuario encontrado'}, status=status.HTTP_404_NOT_FOUND)

#Editar
class EditarUsuarioVista(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id, format=None):
        data = self.request.data
        usuario = get_object_or_404(Usuario, id=id)

        nombreUsuario = data.get('nombreUsuario', None)
        if nombreUsuario is not None:
            usuario.nombreUsuario = nombreUsuario

        ApellidoUsuario1 = data.get('ApellidoUsuario1', None)
        if ApellidoUsuario1 is not None:
            usuario.ApellidoUsuario1 = ApellidoUsuario1

        ApellidoUsuario2 = data.get('ApellidoUsuario2', None)
        if ApellidoUsuario2 is not None:
            usuario.ApellidoUsuario2 = ApellidoUsuario2

        usuario = data.get('usuario', None)
        if usuario is not None:
            usuario.usuario = usuario

        contraseña = data.get('contraseña', None)
        if contraseña is not None:
            usuario.contraseña = contraseña

        rol = data.get('rol', None)
        if rol is not None:
            usuario.rol = rol


        

        usuario.save()

        updated_fields = [key for key in data.keys() if key in [
            'nombreUsuario', 'ApellidoUsuario1', 'ApellidoUsuario2', 'usuario', 'contraseña', 'rol']]
        return Response({'success': 'Usuario editado', 'usuario_id': usuario.id, 'updated_fields': updated_fields})


#Borrar
class BorrarUsuarioVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def delete(self, request, id, format=None):
        usuario = Usuario.objects.get(id=id)
        usuario.delete()
        return Response({'success': 'Usuario eliminado'})
        

#Crear
class CrearUsuarioVista(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # Obtén los datos de la solicitud
        data = request.data

        # Crea una instancia del serializer con los datos
        serializador = UsuarioSerializador(data=data)

        # Valida los datos
        if serializador.is_valid():
            # Guarda el nuevo animal en la base de datos
            serializador.save()

            # Devuelve una respuesta exitosa
            return Response({'success': 'Doctor creado'}, status=200)

        # Devuelve una respuesta con errores de validación si los datos no son válidos
        return Response(serializador.errors, status=404)

