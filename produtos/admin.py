from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'codigo',
        'nome',
        'unidade_medida',
        'preco_venda',
        'ativo',
    )
    list_filter = ('unidade_medida', 'ativo')
    search_fields = ('codigo', 'nome')
