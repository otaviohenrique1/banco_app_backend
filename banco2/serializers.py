from rest_framework import serializers
from .models import Customer, Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["account_number", "balance"]


class CustomerSerializer(serializers.ModelSerializer):
    # Este campo é de leitura apenas porque será criado automaticamente
    account = AccountSerializer()

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "account"]

    def create(self, validated_data):
        # Remover os dados da conta do dicionário principal
        account_data = validated_data.pop("account")
        # Criar o cliente
        customer = Customer.objects.create(**validated_data)
        # Criar a conta associada ao cliente, sem precisar da chave primária
        Account.objects.create(customer=customer, **account_data)
        return customer
