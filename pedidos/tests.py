from decimal import Decimal

from django.db.models.deletion import ProtectedError
from django.test import TestCase

from clientes.models import Cliente
from produtos.models import Produto

from .models import ItemPedidoVenda, PedidoVenda


class PedidoVendaModelTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            tipo_pessoa=Cliente.TipoPessoa.FISICA,
            nome='Carlos da Silva',
            documento='98765432100',
        )
        self.produto = Produto.objects.create(
            codigo='PIS-001',
            nome='Piso intertravado',
            unidade_medida=Produto.UnidadeMedida.METRO_QUADRADO,
            preco_venda='48.00',
        )

    def test_criar_pedido_com_status_orcamento(self):
        pedido = PedidoVenda.objects.create(
            numero_pedido=1,
            cliente=self.cliente,
        )

        self.assertEqual(pedido.status, PedidoVenda.Status.ORCAMENTO)
        self.assertEqual(str(pedido), 'Pedido de venda #1')

    def test_criar_item_de_pedido(self):
        pedido = PedidoVenda.objects.create(
            numero_pedido=1,
            cliente=self.cliente,
        )
        item = ItemPedidoVenda.objects.create(
            pedido=pedido,
            produto=self.produto,
            quantidade='2.00',
            preco_unitario='48.00',
        )

        self.assertEqual(item.pedido, pedido)
        self.assertEqual(item.produto, self.produto)
        self.assertEqual(Decimal(item.quantidade), Decimal('2.00'))

    def test_nao_permitir_apagar_cliente_com_pedido(self):
        PedidoVenda.objects.create(
            numero_pedido=1,
            cliente=self.cliente,
        )

        with self.assertRaises(ProtectedError):
            self.cliente.delete()

    def test_apagar_pedido_apaga_seus_itens(self):
        pedido = PedidoVenda.objects.create(
            numero_pedido=1,
            cliente=self.cliente,
        )
        item = ItemPedidoVenda.objects.create(
            pedido=pedido,
            produto=self.produto,
            quantidade='2.00',
            preco_unitario='48.00',
        )

        pedido.delete()

        self.assertFalse(ItemPedidoVenda.objects.filter(id=item.id).exists())
