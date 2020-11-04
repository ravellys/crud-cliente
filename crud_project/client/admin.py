from django.contrib import admin

from crud_project.client.models import Client


@admin.register(Client)
class ModuloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_cadastro')
    prepopulated_fields = {'slug': ('nome', )}
