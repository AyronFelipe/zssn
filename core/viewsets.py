from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db import transaction
from .serializers import *
from rest_framework import status
from .models import Inventario
from rest_framework.decorators import api_view


class SobreviventeViewSet(viewsets.ViewSet):

    def list(self, request):

        queryset = Sobrevivente.objects.all()
        serializer = SobreviventeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

        data = {}
        with transaction.atomic():

            nome = request.data.get('nome')
            idade = request.data.get('idade')
            sexo = request.data.get('sexo')
            latitude = request.data.get('latitude')
            longitude = request.data.get('longitude')

            if nome == '' or idade == '' or sexo == '' or latitude == '' or longitude == '':
                data['message'] = 'Nenhum dos campos pode ficar em branco.'
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            if len(request.data.get('linhas')) == 0:
                data['message'] = 'Você deve adicionar itens'
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            sobrevivente = Sobrevivente()
            sobrevivente.nome = nome
            sobrevivente.idade = idade
            sobrevivente.sexo = sexo
            sobrevivente.latitude = latitude
            sobrevivente.longitude = longitude

            sobrevivente.save()

            for linha in request.data.get('linhas'):
                item = Item.objects.get(id=linha.get('id'))
                quantidade = int(linha.get('quantidade'))
                Inventario.objects.create(
                    sobrevivente=sobrevivente,
                    item=item,
                    quantidade=quantidade,
                )

            data['message'] = 'Sobrevivente cadastrado com sucesso.'
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(data, status=status.HTTP_200_OK)


class ItemViewset(viewsets.ViewSet):

    def list(self, request):

        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_coordenadas(request, pk):

    data = []
    sobrevivente = Sobrevivente.objects.get(pk=pk)
    data['latitude'] = sobrevivente.latitude
    data['longitude'] = sobrevivente.longitude
    return Response(data, status=status.HTTP_200_OK)
