from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout
from .models import Perfil


def logout_view(request):
    logout(request)
    return redirect('inicio')

# Create your views here.
class UsuarioCreate(CreateView):
    template_name = "cadastros/form.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Garante que o grupo exista mesmo em bancos recém-criados.
        grupo, _ = Group.objects.get_or_create(name="Cliente")
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()

        Perfil.objects.create(usuario=self.object)

        return url

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de novo usuário"
        context['botao'] = "Cadastrar"

        return context

class PerfilUpdate(UpdateView):
    template_name ="cadastros/form.html"
    model = Perfil
    fields = ['nome_completo', 'cpf', 'celular', 'rg', 'nascimento', 'endereco']
    success_url = reverse_lazy('pagina_inicial')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil, usuario=self.request.user)
        return self.object

    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Meus dados pessoais"
        context['botao'] = "Atualizar"

        return context
