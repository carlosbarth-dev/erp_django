from django.contrib import admin

from .models import ItemPedidoVenda, PedidoVenda


class ItemPedidoVendaInline(admin.TabularInline):
    model = ItemPedidoVenda
    extra = 1


@admin.register(PedidoVenda)
class PedidoVendaAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoVendaInline]
    list_display = (
        'numero_pedido',
        'cliente',
        'status',
        'cadastrado_em',
    )
    list_filter = ('status',)
    search_fields = (
        'numero_pedido',
        'cliente__nome',
        'cliente__documento',
    )
