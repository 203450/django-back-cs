from dataclasses import fields
from rest_framework import routers, serializers, viewsets

# importacion de modelos
from UserProfile.models import TableProfile

class TableProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableProfile
        fields = ('pk','id_user','url_image')