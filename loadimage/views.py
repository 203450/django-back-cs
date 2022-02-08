from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions
import os.path
from pathlib import Path

# importaciones de modelos agregados

from loadimage.models import TablaArchivo

# importaciones de serializadores

from loadimage.serializers import TablaArchivoSerializer

# Create your views here.

class LoadFilesTable(APIView):
    def get(self, request, format=None):

        queryset = TablaArchivo.objects.all()
        serializer = TablaArchivoSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "Ningun archivo para subir")
        archivos = request.data['url_img']
        
        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = TablaArchivoSerializer(data=request.data)

        if serializer.is_valid():

            validated_data = serializer.validated_data

            # Guardado de modelo

            img = TablaArchivo(**validated_data)
            img.url_img =  'http://localhost:8000/assets/img/' + str(img.url_img)
            img.save()
            serializer_response = TablaArchivoSerializer(img)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoadFilesTableDetail(APIView):

    def get_object(self, pk):

        try:
            return TablaArchivo.objects.get(pk = pk)
        except TablaArchivo.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):

        idResponse = self.get_object(pk)

        if idResponse != 0:
            idResponse = TablaArchivoSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, format=None):

        idResponse = self.get_object(pk)
        archivos = request.data['url_img']
        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato

        serializer = TablaArchivoSerializer(idResponse, data = request.data)

        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        
        imagen = self.get_object(pk)
        if imagen != 0:
            imagen.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Datos no encontrados",status = status.HTTP_400_BAD_REQUEST) 