from django.urls import path
from .views import IndexView, BuscarView, PaginaInicialView, ContatoView, PoliticaView, ServicoView, SobreNosView, SuporteView, MeusDadosView

urlpatterns = [
    path('', IndexView.as_view(), name = 'inicio'),
    path('pagina_inicial/', PaginaInicialView.as_view(), name = 'pagina_inicial'),
    path('contato/', ContatoView.as_view(), name = 'contato'),
    path('buscar/', BuscarView.as_view(), name = 'buscar'),
    path('politica/', PoliticaView.as_view(), name = 'politica'),
    path('servico/', ServicoView.as_view(), name = 'servico'),
    path('sobrenos/', SobreNosView.as_view(), name = 'sobrenos'),
    path('suporte/', SuporteView.as_view(), name = 'suporte'),
    path('meusdados/', MeusDadosView.as_view(), name = 'meusdados'),
]