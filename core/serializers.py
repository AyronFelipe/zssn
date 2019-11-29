from rest_framework import serializers
from .models import Sobrevivente


class SobreviventeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sobrevivente
        fields = [
            'nome',
            'idade',
            'sexo',
            'latitude',
            'longitude',
        ]
