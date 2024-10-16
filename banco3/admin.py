from django.contrib import admin


class Clientes(admin.ModelAdmin):
    list_display = (
        "nome",
        "email",
        "senha",
        "cpf",
    )
    list_display_links = (
        "id",
        "nome",
    )
    list_per_page = 20
    search_fields = (
        "nome",
        "cpf",
    )
    ordering = ("nome",)


class Contas(admin.ModelAdmin):
    list_display = (
        "saldo",
        "agencia",
        "banco",
        "conta_numero",
        "nome_banco",
    )
    list_display_links = (
        "id",
        "saldo",
    )
    list_per_page = 20
    search_fields = ("conta",)
    ordering = ("conta",)


class Cartoes(admin.ModelAdmin):
    list_display = (
        "nome",
        "numero",
        "validade",
        "cvv",
        "tipo",
        "cliente",
    )
    list_display_links = (
        "id",
        "numero",
    )
    list_per_page = 20
    search_fields = ("numero",)
    ordering = ("numero",)