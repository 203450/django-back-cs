from multiprocessing import context
from django.http import response
from django.shortcuts import render

# Recursos de rest-framework
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# Create your views here.
class LoginAuth(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        token,create=Token.objects.get_or_create(user=user)

        print(user.pk)

        return Response({
            'token':token.key,
            'username':user.username,
            'user_id':user.pk,
            'email':user.email
        })