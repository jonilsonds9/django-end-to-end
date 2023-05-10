from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.listar, name='listar'),
    path('detalhes/<int:cliente_id>', views.detalhes, name='detalhes'),
    path('cadastro', views.cadastrar, name='cadastrar'),
]
