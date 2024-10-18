from rest_framework import serializers
from banco3.models import Conta2, Cliente2, Cartao2
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate

class Conta2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Conta2
        fields = ["id", "saldo", "agencia", "banco", "conta_numero", "nome_banco"]


class Cliente2Serializer(serializers.ModelSerializer):
    conta = Conta2Serializer()

    class Meta:
        model = Cliente2
        fields = ["id", "nome", "email", "senha", "cpf", "conta"]
    
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
        fields = ["id", "nome", "numero", "validade", "cvv", "tipo", "cliente"]


class LoginSerializer(serializers.Serializer):
    cpf = serializers.CharField()
    senha = serializers.CharField()

    def validate(self, data):
        cpf = data.get('cpf')
        senha = data.get('senha')
        try:
            cliente = Cliente2.objects.get(cpf=cpf)
        except Cliente2.DoesNotExist:
            raise serializers.ValidationError('CPF ou senha inválidos.')
        
        if not check_password(senha, cliente.senha):
            # print(f"senha {senha}")
            # print(f"senha {cliente.senha}")
            raise serializers.ValidationError('CPF ou senha inválidos. asd')

        # print("----------------")
        # print(f"{cliente}")
        # print("----------------")
        return {'cliente': cliente}
