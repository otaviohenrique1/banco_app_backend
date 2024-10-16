"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# from banco.views import CartaoViewSet, ClienteViewSet, ContaViewSet
from banco2.views import CustomerViewSet
from banco3.views import Cartao2ViewSet, Cliente2ViewSet, Conta2ViewSet, LoginView

router = routers.DefaultRouter()
router.register("contas", Conta2ViewSet, basename="contas")
router.register("clientes", Cliente2ViewSet, basename="clientes")
router.register("cartoes", Cartao2ViewSet, basename="cartoes")
router.register("customers", CustomerViewSet, basename="customers")
# router.register("clientes2", Cliente2ViewSet, basename="clientes2")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    # path('login/', LoginView2.as_view(), name='login')
    path("login/", LoginView.as_view(), name="login"),
]
