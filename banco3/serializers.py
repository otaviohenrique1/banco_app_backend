from rest_framework import serializers
from banco3.models import Conta2, Cliente2, Cartao2
from django.contrib.auth.hashers import make_password

class Conta2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Conta2
        fields = ["saldo", "agencia", "banco", "conta_numero", "nome_banco"]


class Cliente2Serializer(serializers.ModelSerializer):
    conta = Conta2Serializer()

    class Meta:
        model = Cliente2
        fields = ["nome", "email", "senha", "cpf", "conta"]
    
    def create(self, validated_data):
        conta_data = validated_data.pop("conta")
        cliente = Cliente2.objects.create(**validated_data)
        Conta2.objects.create(cliente=cliente, **conta_data)
        return cliente
    
    def validate_senha(self, value):
        return make_password(value)


class Cartao2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Cartao2
        fields = ["nome", "numero", "validade", "cvv", "tipo", "cliente"]