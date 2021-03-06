from django.db import models
from django.conf import settings


class Sobrevivente(models.Model):

    MASCULINO = 'M'
    FEMININO = 'F'
    OUTRO = 'O'

    SEXO = (
        (MASCULINO, 'Masculino'),
        (FEMININO, 'Feminino'),
        (OUTRO, 'Outro'),
    )

    nome = models.CharField('Nome', max_length=255, null=True, blank=True)
    idade = models.IntegerField('Idade', null=True, blank=True)
    sexo = models.CharField('Sexo', max_length=1, null=True, blank=True, choices=SEXO)
    latitude = models.CharField('Latitude', max_length=12, null=True, blank=True)
    longitude = models.CharField('Latitude', max_length=12, null=True, blank=True)
    infectado = models.BooleanField('Está infectado?', default=False)
    votos = models.IntegerField('Votos', null=True, blank=True, default=0)

    def __str__(self):

        return self.nome
    
    def atualizar(self):

        if self.votos >= settings.NUMERO_VOTOS:
            self.infectado = True
            self.save()


class Item(models.Model):

    nome = models.CharField('Nome', max_length=255, null=True, blank=True)
    valor = models.IntegerField('Valor', null=True, blank=True)

    def __str__(self):

        return "%s - %s" % (self.nome, self.valor)


class Inventario(models.Model):

    item = models.ForeignKey(Item, on_delete=models.SET_NULL, related_name='item_sobreviventes', null=True, blank=True)
    sobrevivente = models.ForeignKey(Sobrevivente, on_delete=models.SET_NULL, related_name='sobrevivente_itens', null=True, blank=True)
    quantidade = models.IntegerField('Quantidade', null=True, blank=True)

    def __str__(self):

        return '%s do(a) %s' % (self.item, self.sobrevivente)
