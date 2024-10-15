from django.contrib import admin


class Contas(admin.ModelAdmin):
    list_display = (
        "id",
        "saldo",
        "agencia",
        "banco",
        "conta",
        "nome_banco",
    )
    list_display_links = (
        "id",
        "saldo",
    )
    list_per_page = 20
    search_fields = ("conta",)
    ordering = ("conta",)


class Clientes(admin.ModelAdmin):
    list_display = (
        "id",
        "nome",
        "email",
        "senha",
        "cpf",
        "conta",
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


class Cartoes(admin.ModelAdmin):
    list_display = (
        "id",
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
