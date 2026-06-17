from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    nome_completo = models.CharField(max_length = 100, null=True)
    cpf = models.CharField(max_length = 14, null=True)
    celular = models.CharField(max_length = 17, null=True)
    rg = models.CharField(max_length = 17, null=True)
    nascimento = models.DateField(null=True)
    endereco = models.CharField(max_length = 100, null=True)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
