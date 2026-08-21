from django.db import IntegrityError
from django.test import TestCase

from .admin import ClienteAdminForm
from .models import Cliente


class ClienteModelTest(TestCase):
    def test_criar_cliente_valido(self):
        cliente = Cliente.objects.create(
            tipo_pessoa=Cliente.TipoPessoa.FISICA,
            nome='João da Silva',
            documento='12345678900',
        )

        self.assertEqual(cliente.nome, 'João da Silva')
        self.assertEqual(cliente.documento, '12345678900')
        self.assertEqual(cliente.ativo, True)

    def test_rejeitar_cpf_com_tamanho_invalido(self):
        formulario = ClienteAdminForm(
            data={
                'tipo_pessoa': Cliente.TipoPessoa.FISICA,
                'nome': 'Maria da Silva',
                'documento': '123',
            }
        )

        self.assertFalse(formulario.is_valid())
        self.assertIn(
            'CPF deve ter 11 numeros.',
            formulario.errors['documento'],
        )

    def test_rejeitar_documento_com_letras(self):
        formulario = ClienteAdminForm(
            data={
                'tipo_pessoa': Cliente.TipoPessoa.JURIDICA,
                'nome': 'Pedro Santos',
                'documento': '1234567890A',
            }
        )

        self.assertFalse(formulario.is_valid())
        self.assertIn(
            'Informe somente numeros.',
            formulario.errors['documento'],
        )

    def test_rejeitar_cnpj_com_tamanho_invalido(self):
        formulario = ClienteAdminForm(
            data={
                'tipo_pessoa': Cliente.TipoPessoa.JURIDICA,
                'nome': 'Construtora Horizonte',
                'documento': '1234567890123',
            }
        )

        self.assertFalse(formulario.is_valid())
        self.assertIn(
            'CNPJ deve ter 14 numeros.',
            formulario.errors['documento'],
        )

    def test_rejeitar_documento_duplicado(self):
        Cliente.objects.create(
            tipo_pessoa=Cliente.TipoPessoa.FISICA,
            nome='Primeiro Cliente',
            documento='12345678900',
        )

        with self.assertRaises(IntegrityError):
            Cliente.objects.create(
                tipo_pessoa=Cliente.TipoPessoa.FISICA,
                nome='Segundo Cliente',
                documento='12345678900',
            )
