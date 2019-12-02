from django.test import TestCase

from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key

from .models import Sobrevivente

class SobreviventeTestModel(TestCase):

    def setUp(self):

        self.sobrevivente = mommy.make(Sobrevivente)