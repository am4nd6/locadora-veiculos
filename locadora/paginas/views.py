from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'paginas/index.html'

class PaginaInicialView(TemplateView):
    template_name = 'paginas/pagina_inicial.html'


class BuscarView(TemplateView):
    template_name = 'paginas/buscar.html'

class ContatoView(TemplateView):
    template_name = 'paginas/contato.html'

class PoliticaView(TemplateView):
    template_name = 'paginas/politica.html'

class ServicoView(TemplateView):
    template_name = 'paginas/servico.html'

class SobreNosView(TemplateView):
    template_name = 'paginas/sobrenos.html'

class SuporteView(TemplateView):
    template_name = 'paginas/suporte.html'

class MeusDadosView(TemplateView):
    template_name = 'paginas/perfil.html'
