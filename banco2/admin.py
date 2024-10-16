from django.contrib import admin


class Clientes(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "email",
    )
    list_display_links = (
        "id",
        "first_name",
        "last_name",
        "email",
    )
    list_per_page = 20
    search_fields = (
        "first_name",
        "last_name",
    )
    ordering = (
        "nome",
        "last_name",
    )


class Clientes(admin.ModelAdmin):
    list_display = (
        "id",
        "customer",
        "account_number",
        "balance",
    )
    list_display_links = (
        "id",
        "account_number",
    )
    list_per_page = 20
    search_fields = ("account_number",)
    ordering = ("account_number",)
