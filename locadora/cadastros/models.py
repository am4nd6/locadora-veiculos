from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Veiculos(models.Model):
    CARRO = 'car'
    VAN = 'van'
    MOTO = 'moto'
    TIPO_CHOICES = [
        (CARRO, 'Carro'),
        (VAN, 'Van'),
        (MOTO, 'Moto'),
    ]
    placa = models.CharField(max_length = 10)
    modelo = models.CharField(max_length = 100)
    marca = models.CharField(max_length = 100)
    ano = models.PositiveBigIntegerField()
    cor = models.CharField(max_length = 100)
    tipo = models.CharField(
        max_length=4,
        choices=TIPO_CHOICES,
        default=CARRO,
    )
    preco_diaria = models.DecimalField(max_digits=5, decimal_places=2, default=45)
    usuario = models.ForeignKey(User, on_delete= models.PROTECT)

    def __str__(self):
        return "Placa: {} Modelo: {} Marca: {} Ano: {} Cor: {} Tipo: {} Preço Diária: {}".format(self.placa, self.modelo, self.marca, self.ano, self.cor, self.tipo, self.preco_diaria)

class Alugados(models.Model):
    veiculo = models.ForeignKey("Veiculos", on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return " Veiculo: {} Data início: {} Data Final: {} Valor total: {} Devolvido? {}".format(self.veiculo, self.data_inicio, self.data_fim, self.valor_total, self.devolvido)
