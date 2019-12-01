from rest_framework import serializers
from .models import Sobrevivente, Item


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


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'pk',
            'nome',
            'valor',
        ]
