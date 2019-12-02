from django.contrib import admin
from django.urls import path, include
from .routers import router
from core.viewsets import get_coordenadas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls), name='api'),
    path('', include('core.urls')),
    path('api/sobrevivente/<int:pk>/coordenadas/', get_coordenadas, name='get_coordenadas'),
]
