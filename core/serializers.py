from rest_framework import serializers
from .models import Sobrevivente, Item, Inventario


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


class InventarioSerializer(serializers.ModelSerializer):

    valor = serializers.SerializerMethodField()
    item_nome = serializers.SerializerMethodField()
    quantidade_total = serializers.SerializerMethodField()

    class Meta:
        model = Inventario
        fields = [
            'item',
            'quantidade',
            'valor',
            'item_nome',
            'pk',
            'quantidade_total',
        ]

    def get_valor(self, obj):

        return obj.item.valor

    def get_item_nome(self, obj):

        return obj.item.nome

    def get_quantidade_total(self, obj):

        return obj.quantidade
