from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db import transaction
from .serializers import SobreviventeSerializer, Sobrevivente
from rest_framework import status


class SobreviventeViewSet(viewsets.ViewSet):

    def list(self, request):

        queryset = Sobrevivente.objects.all()
        serializer = SobreviventeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):

        data = {}
        with transaction.atomic():

            nome = request.POST.get('nome')
            idade = request.POST.get('idade')
            sexo = request.POST.get('sexo')
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')

            if nome == '' or idade == '' or sexo == '' or latitude == '' or longitude == '':
                data['mensagem'] = 'Nenhum dos campos pode ficar em branco.'
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            sobrevivente = Sobrevivente()
            sobrevivente.nome = nome
            sobrevivente.idade = idade
            sobrevivente.sexo = sexo
            sobrevivente.latitude = latitude
            sobrevivente.longitude = longitude

            sobrevivente.save()

            data['mensagem'] = 'Sobrevivente cadastrado com sucesso.'
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(data, status=status.HTTP_200_OK)