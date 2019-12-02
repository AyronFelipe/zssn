from django.contrib import admin
from django.urls import path, include
from .routers import router
from core.viewsets import get_coordenadas, informar_infectado, sobreviventes_totais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
    path('', include('core.urls')),
    path('api/sobrevivente/<int:pk>/coordenadas/', get_coordenadas, name='get_coordenadas'),
    path('api/sobrevivente/<int:pk>/infectado/', informar_infectado, name='informar_infectado'),
    path('api/sobreviventes-totais/', sobreviventes_totais, name='sobreviventes_totais'),
]
