from django.db import models


class Conta(models.Model):
    saldo = models.DecimalField(
        max_digits=20, decimal_places=2, null=False, blank=False
    )
    agencia = models.IntegerField(max_length=4, null=False, blank=False)
    banco = models.IntegerField(max_length=4, null=False, blank=False)
    conta = models.IntegerField(max_length=10, null=False, blank=False)
    nome_banco = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.saldo}"


class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)
    senha = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.cpf}"


class Cartao(models.Model):
    TIPO = (
        ("F", "Fisico"),
        ("T", "Temporario"),
        ("V", "Virtual"),
    )

    nome = models.CharField(max_length=4, null=False, blank=False)
    numero = models.CharField(max_length=4, null=False, blank=False)
    validade = models.CharField(max_length=10, null=False, blank=False)
    cvv = models.CharField(max_length=255, null=False, blank=False)
    tipo = models.CharField(max_length = 1, choices = TIPO, blank = False, null = False, default = 'F')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} - {self.numero} - {self.cvv} - {self.validade}"
