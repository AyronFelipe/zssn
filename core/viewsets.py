from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.db import transaction
from .serializers import *
from rest_framework import status
from .models import Inventario
from rest_framework.decorators import api_view
from django.db.models import Count


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
    
    def update(self, request, pk=None):

        data = {}
        try:
            sobrevivente = Sobrevivente.objects.get(pk=pk)
        except:
            data['message'] = 'Sobrevivente não encontrado.'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        if latitude == '' or longitude == '':
            data['message'] = 'Nenhum dos campos pode ficar em branco.'
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        
        sobrevivente.latitude = latitude
        sobrevivente.longitude = longitude
        sobrevivente.save()

        data['message'] = 'Dados alterados com sucesso'
        return Response(data, status=status.HTTP_200_OK)


class ItemViewset(viewsets.ViewSet):

    def list(self, request):

        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_coordenadas(request, pk):

    data = {}
    try:
        sobrevivente = Sobrevivente.objects.get(pk=pk)
    except:
        data['message'] = 'Sobrevivente não encontrado'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    data['latitude'] = sobrevivente.latitude
    data['longitude'] = sobrevivente.longitude
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def informar_infectado(request, pk):

    data = {}
    try:
        sobrevivente = Sobrevivente.objects.get(pk=pk)
    except:
        data['message'] = 'Sobrevivente não encontrado'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    voto = sobrevivente.votos + 1
    sobrevivente.votos = voto
    sobrevivente.save()

    data['message'] = 'Obrigado por nos informar. O apocalipse zumbi é muito difícil mesmo.'
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def sobreviventes_totais(request):

    data = {}
    sobreviventes = []
    for sobrevivente in Sobrevivente.objects.all():
        sobrevivente.atualizar()
        sobreviventes.append(sobrevivente)
    serializer = SobreviventesTotaisSerializer(sobreviventes, many=True)
    data['sobreviventes'] = serializer.data
    data['porcentagem_sobreviventes_nao_infectados'] = ((100 * Sobrevivente.objects.filter(infectado=False).count()) / Sobrevivente.objects.all().count())
    data['porcentagem_sobreviventes_infectados'] = ((100 * Sobrevivente.objects.filter(infectado=True).count()) / Sobrevivente.objects.all().count())
    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def itens_sobrevivente(request, pk):

    data = {}
    try:
        sobrevivente = Sobrevivente.objects.get(pk=pk)
    except:
        data['message'] = 'Sobrevivente não encontrado'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    queryset = sobrevivente.sobrevivente_itens.all()
    serializer = InventarioSerializer(queryset, many=True)
    data['itens'] = serializer.data
    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
def trocar_itens(request):

    data = {}
    try:
        sobrevivente1 = Sobrevivente.objects.get(pk=request.data.get('sobrevivente1'))
    except:
        data['message'] = 'Sobrevivente 1 não encontrado'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    try:
        sobrevivente2 = Sobrevivente.objects.get(pk=request.data.get('sobrevivente2'))
    except:
        data['message'] = 'Sobrevivente 2 não encontrado'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    if sobrevivente1 == sobrevivente2:
        data['message'] = 'Os sobreviventes da transação não podem ser os mesmos.'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    total1 = 0
    for item in request.data.get('itens1'):
        multi = item.get('quantidade') * item.get('valor')
        total1 = total1 + multi

    total2 = 0
    for item in request.data.get('itens2'):
        multi = item.get('quantidade') * item.get('valor')
        total2 = total2 + multi

    if total1 != total2:
        data['message'] = 'Os itens não possuem o mesmo valor.'
        return Response(data, status=status.HTTP_400_BAD_REQUEST)

    for item in request.data.get('itens1'):
        item_obj = Item.objects.get(pk=item.get('item'))
        Inventario.objects.create(
            sobrevivente=sobrevivente2,
            item=item_obj,
            quantidade=item.get('quantidade')
        )
        inventario_antigo = Inventario.objects.get(pk=item.get('pk'))
        sub = inventario_antigo.quantidade - item.get('quantidade')
        inventario_antigo.quantidade = sub
        inventario_antigo.save()
    
    for item in request.data.get('itens2'):
        item_obj = Item.objects.get(pk=item.get('item'))
        Inventario.objects.create(
            sobrevivente=sobrevivente1,
            item=item_obj,
            quantidade=item.get('quantidade')
        )
        inventario_antigo = Inventario.objects.get(pk=item.get('pk'))
        sub = inventario_antigo.quantidade - item.get('quantidade')
        inventario_antigo.quantidade = sub
        inventario_antigo.save()
    
    data['message'] = 'Itens trocados com sucesso!'
    return Response(data, status=status.HTTP_200_OK)

    return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def sobreviventes_infectados(request):

    queryset = Sobrevivente.objects.filter(infectado=True)
    serializer = SobreviventesTotaisSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def sobreviventes_nao_infectados(request):

    queryset = Sobrevivente.objects.filter(infectado=False)
    serializer = SobreviventesTotaisSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def media_recurso(request):

    lol = []
    for item in Item.objects.all():
        quantidade = 0
        for obj in item.item_sobreviventes.all():
            if obj.sobrevivente.infectado is not True:
                quantidade = quantidade + obj.quantidade
        lol.append({
            'nome': item.nome,
            'media': quantidade / Sobrevivente.objects.filter(infectado=False).count()
        })
    return Response(lol, status=status.HTTP_200_OK)
