from django.urls import path, include
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('documentacao/', schema_view),
]