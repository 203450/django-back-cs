from dataclasses import fields
from rest_framework import serializers

# importacion de modelos
from UserProfile.models import TableProfile

class TableProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableProfile
        fields = ('id_user','url_image')