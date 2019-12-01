from rest_framework.routers import DefaultRouter
from core import viewsets as core_viewsets

router = DefaultRouter()
router.register(r'sobreviventes', core_viewsets.SobreviventeViewSet, base_name='sobreviventes')
router.register(r'itens', core_viewsets.ItemViewset, base_name='itens')
