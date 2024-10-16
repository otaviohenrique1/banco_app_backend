from rest_framework import serializers
from banco.models import Conta, Cliente, Cartao


class ContaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conta
        fields = [
            "id",
            "saldo",
            "agencia",
            "banco",
            "conta",
            "nome_banco",
            "cliente",
        ]


class ClienteSerializer(serializers.ModelSerializer):
    conta = ContaSerializer()

    class Meta:
        model = Cliente
        fields = [
            "id",
            "nome",
            "email",
            "senha",
            "cpf",
            "conta",
        ]

    def create(self, validated_data):
        conta_data = validated_data.pop("conta")
        cliente = Cliente.objects.create(**validated_data)
        Conta.objects.create(cliente=cliente, **conta_data)
        return cliente


class CartaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao
        fields = ["id", "nome", "numero", "validade", "cvv", "tipo", "cliente"]
