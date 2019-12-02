from django.contrib import admin
from django.urls import path, include
from .routers import router
from core.viewsets import get_coordenadas, informar_infectado, sobreviventes_totais, itens_sobrevivente, trocar_itens, \
sobreviventes_infectados, sobreviventes_nao_infectados, media_recurso

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
    path('', include('core.urls')),
    path('api/sobrevivente/<int:pk>/coordenadas/', get_coordenadas, name='get_coordenadas'),
    path('api/sobrevivente/<int:pk>/infectado/', informar_infectado, name='informar_infectado'),
    path('api/sobreviventes-totais/', sobreviventes_totais, name='sobreviventes_totais'),
    path('api/sobrevivente/<int:pk>/itens/', itens_sobrevivente, name='itens_sobrevivente'),
    path('api/trocar-itens/', trocar_itens, name='trocar_itens'),
    path('api/sobreviventes-infectados/', sobreviventes_infectados, name='sobreviventes_infectados'),
    path('api/sobreviventes-nao-infectados/', sobreviventes_nao_infectados, name='sobreviventes_nao_infectados'),
    path('api/media-recurso/', media_recurso, name='media_recurso'),
]
