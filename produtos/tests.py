from decimal import Decimal

from django.db import IntegrityError
from django.test import TestCase

from .models import Produto


class ProdutoModelTest(TestCase):
    def test_criar_produto_valido(self):
        produto = Produto.objects.create(
            codigo='LAJ-H8',
            nome='Laje H8',
            unidade_medida=Produto.UnidadeMedida.METRO_QUADRADO,
            preco_venda='85.00',
        )

        self.assertEqual(str(produto), 'LAJ-H8 - Laje H8')
        self.assertEqual(Decimal(produto.preco_venda), Decimal('85.00'))
        self.assertEqual(produto.ativo, True)

    def test_codigo_do_produto_deve_ser_unico(self):
        Produto.objects.create(
            codigo='LAJ-H8',
            nome='Laje H8',
            unidade_medida=Produto.UnidadeMedida.METRO_QUADRADO,
            preco_venda='85.00',
        )

        with self.assertRaises(IntegrityError):
            Produto.objects.create(
                codigo='LAJ-H8',
                nome='Outra Laje H8',
                unidade_medida=Produto.UnidadeMedida.METRO_QUADRADO,
                preco_venda='90.00',
            )
