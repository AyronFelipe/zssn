from django.db import models


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
    latitude = models.CharField('Latitude', max_length=10, null=True, blank=True)
    longitude = models.CharField('Latitude', max_length=10, null=True, blank=True)

    def __str__(self):

        return self.nome
