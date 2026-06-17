from django.urls import path
from .views import VeiculosCreate, AlugadosCreate, VeiculosUpdate, AlugadosUpdate, VeiculosDelete, AlugadosDelete, VeiculosList, AlugadosList

urlpatterns = [
    path('cadastrar/veiculos/', VeiculosCreate.as_view(), name = 'cadastrar-veiculos'),
    path('cadastrar/alugados/', AlugadosCreate.as_view(), name = 'cadastrar-alugados'),

    path('editar/veiculos/<int:pk>/', VeiculosUpdate.as_view(), name = 'editar-veiculos'),
    path('editar/alugados/<int:pk>/', AlugadosUpdate.as_view(), name = 'editar-alugados'),

    path('excluir/veiculos/<int:pk>/', VeiculosDelete.as_view(), name = 'excluir-veiculos'),
    path('excluir/alugados/<int:pk>/', AlugadosDelete.as_view(), name = 'excluir-alugados'),
    
    path('listar/veiculos/', VeiculosList.as_view(), name = 'listar-veiculos'),
    path('listar/alugados/', AlugadosList.as_view(), name = 'listar-alugados'),
]