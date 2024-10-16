from django.shortcuts import render
from rest_framework import viewsets, filters, status
from banco3.models import Conta2, Cliente2, Cartao2
from banco3.serializers import Conta2Serializer, Cliente2Serializer, Cartao2Serializer, LoginSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken

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


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cliente = serializer.validated_data['cliente']
        token = AuthToken.objects.create(user=cliente)
        return Response({
            'token': token.token,
            'cliente_id': cliente.pk,
            'cpf': cliente.cpf
        }, status=status.HTTP_200_OK)