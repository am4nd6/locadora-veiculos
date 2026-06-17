from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Veiculos, Alugados
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.shortcuts import get_object_or_404
# Create your views here.

class VeiculosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url= reverse_lazy('login')
    group_required = u"Administrador"
    model = Veiculos
    fields = ['placa', 'modelo', 'marca', 'ano', 'cor', 'tipo', 'preco_diaria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-veiculos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Cadastro de Veículos"
        context['botao'] = "Cadastrar"
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url


class AlugadosCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url= reverse_lazy('login')
    group_required = u"Administrador"
    model = Alugados
    fields = ['cliente', 'data_inicio', 'data_fim', 'valor_total', ' devolvido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-alugados')

class VeiculosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url= reverse_lazy('login')
    group_required = u"Administrador"
    model = Veiculos
    fields = ['placa', 'modelo', 'marca', 'ano', 'cor', 'tipo', 'preco_diaria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-veiculos')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Editar cadastro de Veículo"
        context['icone'] = '<i class="fa fa-check" aria-hidden="true"></i>'
        context['botao'] = "Salvar"
        return context

    def get_object(self, queryset= None):
        self.object = get_object_or_404(Veiculos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class AlugadosUpdate(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url= reverse_lazy('login')
    group_required = u"Administrador"
    model = Alugados
    fields = ['cliente', 'data_inicio', 'data_fim', 'valor_total', ' devolvido']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-alugados')

class VeiculosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url= reverse_lazy('login')
    group_required = u"Administrador"
    model = Veiculos
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-veiculos')

    def get_object(self, queryset= None):
        self.object = get_object_or_404(Veiculos, pk=self.kwargs['pk'], usuario=self.request.user)
        return self.object


class AlugadosDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url= reverse_lazy('login')
    group_required = u"Administrador"
    model = Alugados
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-alugados')

class VeiculosList(LoginRequiredMixin,ListView):
    login_url= reverse_lazy('login')
    model = Veiculos
    template_name = 'cadastros/listas/veiculos.html'


class AlugadosList(LoginRequiredMixin, ListView):
    login_url= reverse_lazy('login')
    model = Alugados
    template_name = 'cadastros/listas/alugados.html'
    paginate_by = 30