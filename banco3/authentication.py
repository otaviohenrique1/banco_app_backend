from django.contrib.auth.backends import ModelBackend
from banco3.models import Cliente2  # Seu modelo de cliente personalizado

class CPFBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Tenta autenticar o usuário com base no CPF
            user = Cliente2.objects.get(cpf=username)
            if user.check_password(password):
                return user
        except Cliente2.DoesNotExist:
            return None