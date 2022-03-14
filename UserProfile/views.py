from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asyncio import exceptions
import os.path
from django.contrib.auth.models import User

#Importaciones de modelos
from UserProfile.models import TableProfile

#Importaciones de serializadores
from UserProfile.serializers import TableProfileSerializer

# Create your views here.

class TableProfileList(APIView):

    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 404
    
    def get(self,request,format=None):
        queryset=TableProfile.objects.all()
        serializer = TableProfileSerializer(queryset,many=True,context={'request':request})
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        
        serializer=TableProfileSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            validated_data = serializer.validated_data
            img = TableProfile(**validated_data)
            serializer_response = TableProfileSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class TableProfileDetail(APIView):
    
    def get_object(self, pk):
        try:
            return TableProfile.objects.get(id_user = pk)
        except TableProfile.DoesNotExist:
            return 404

    def res_custom(self, user, data, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "id_user" : data.get('id_user'),
            "url_image" : data.get('url_image'),
            "status" : status
        }
        return response;

    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        user = User.objects.filter(id=pk).values()
        if idResponse != 404:
            idResponse = TableProfileSerializer(idResponse)
            responseOK = self.res_custom(user,idResponse.data,status.HTTP_200_OK)
            return Response(responseOK)
        else:
            errorData={
                "url_image": "/img/Default.jpg",
                "id_user" : pk,  
            }
        responseOK = self.res_custom(user, errorData,status.HTTP_400_BAD_REQUEST)
        return Response(responseOK)

    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        serializer = TableProfileSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas,status =status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class DataProfileDetail(APIView):
    
    def res_custom(self, user, status):

        response = {

            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "status" : status
        }
        return response
    
    def get(self, request, pk, format=None):

        idResponse = User.objects.filter(id=pk).values()
        if(idResponse != 404):
            responseData = self.res_custom(idResponse, status.HTTP_200_OK)
            return Response(responseData)
        return("No se encontró el usuario")
    
    def put(self, request, pk, format=None):
        
        data = request.data
        user = User.objects.filter(id = pk)

        if(data.get("first_name") != ""):
            user.update(first_name = data.get('first_name'))
        
        if(data.get("last_name") != ""):
            user.update(last_name = data.get('last_name'))

        if(data.get("username") != ""):
            user.update(username = data.get('username'))

        if(data.get("email") != ""):
            user.update(email = data.get('email'))
            
        user2 = User.objects.filter(id=pk).values()
        return Response(self.res_custom(user2, status.HTTP_200_OK))

    

