from django.shortcuts import render
from rest_framework import viewsets, filters
from banco.models import Cartao, Cliente, Conta
from banco.serializers import CartaoSerializer, ClienteSerializer, ContaSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ContaViewSet(viewsets.ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["conta"]


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["nome", "cpf"]


class CartaoViewSet(viewsets.ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["numero"]
