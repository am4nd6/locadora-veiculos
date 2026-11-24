from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UsuarioForm(UserCreationForm):
    username = forms.CharField(
        label='Nome de usuário',
        max_length=150,
        help_text='150 caracteres ou menos. Letras, números e @/./+/-/_ apenas.',
    )
    email = forms.EmailField(label='E-mail', max_length=100)
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        widget=forms.PasswordInput,
        help_text='Sua senha deve ter pelo menos 8 caracteres e não pode ser comum, totalmente numérica ou muito parecida com suas informações pessoais.',
    )
    password2 = forms.CharField(
        label='Confirmação de senha',
        strip=False,
        widget=forms.PasswordInput,
        help_text='Digite a mesma senha novamente para confirmação.',
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        e = self.cleaned_data['email']
        if User.objects.filter(email=e).exists():
            raise ValidationError("O email {} já está em uso.".format(e))
            
        return e
