from rest_framework import serializers
from .models import Sobrevivente, Item


class SobreviventeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sobrevivente
        fields = [
            'nome',
            'pk',
        ]


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = [
            'pk',
            'nome',
            'valor',
        ]


class SobreviventesTotaisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sobrevivente
        fields = [
            'pk',
            'nome',
            'latitude',
            'longitude',
            'idade',
            'infectado',
        ]
