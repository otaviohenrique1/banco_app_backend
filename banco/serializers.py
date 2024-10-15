from rest_framework import serializers
from banco.models import Conta, Cliente, Cartao


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = ["id", "saldo", "agencia", "banco", "conta", "nome_banco"]


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ["id", "nome", "email", "senha", "cpf", "conta"]


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ["id", "nome", "numero", "validade", "cvv", "tipo", "cliente"]
