from django.db import models

from clientes.models import Cliente
from produtos.models import Produto


class PedidoVenda(models.Model):
    class Status(models.TextChoices):
        ORCAMENTO = 'ORCAMENTO', 'Orcamento'
        ABERTO = 'ABERTO', 'Aberto'
        FINALIZADO = 'FINALIZADO', 'Finalizado'
        CANCELADO = 'CANCELADO', 'Cancelado'

    numero_pedido = models.PositiveIntegerField(unique=True)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='pedidos_venda',
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.ORCAMENTO,
    )
    observacoes = models.TextField(blank=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pedido de venda #{self.numero_pedido}'

    class Meta:
        ordering = ['-cadastrado_em']
        verbose_name = 'Pedido de venda'
        verbose_name_plural = 'Pedidos de venda'


class ItemPedidoVenda(models.Model):
    pedido = models.ForeignKey(
        PedidoVenda,
        on_delete=models.CASCADE,
        related_name='itens',
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,
        related_name='itens_pedido_venda',
    )
    quantidade = models.DecimalField(max_digits=10, decimal_places=2)
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.produto} - {self.quantidade}'

    class Meta:
        verbose_name = 'Item do pedido de venda'
        verbose_name_plural = 'Itens do pedido de venda'
