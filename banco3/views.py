from django.shortcuts import render
from rest_framework import viewsets, filters
from banco3.models import Conta2, Cliente2, Cartao2
from banco3.serializers import Conta2Serializer, Cliente2Serializer, Cartao2Serializer
from django_filters.rest_framework import DjangoFilterBackend


class Conta2ViewSet(viewsets.ModelViewSet):
    queryset = Conta2.objects.all()
    serializer_class = Conta2Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["conta_numero"]


class Cliente2ViewSet(viewsets.ModelViewSet):
    queryset = Cliente2.objects.all()
    serializer_class = Cliente2Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["nome", "cpf"]


class Cartao2ViewSet(viewsets.ModelViewSet):
    queryset = Cartao2.objects.all()
    serializer_class = Cartao2Serializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["numero"]
    
