from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    email = models.CharField(max_length=255, null=False, blank=False, unique=True)
    senha = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)

    def __str__(self):
        return f"{self.nome} - {self.email} - {self.cpf}"


class Conta(models.Model):
    saldo = models.FloatField(max_length=20, null=False, blank=False)
    agencia = models.CharField(max_length=4, null=False, blank=False)
    banco = models.CharField(max_length=4, null=False, blank=False)
    conta = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f"{self.saldo}"


class Banco(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    agencia = models.CharField(max_length=255, null=False, blank=False)
    banco = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.nome} - {self.agencia} - {self.banco}"
