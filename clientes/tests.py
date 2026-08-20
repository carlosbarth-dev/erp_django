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
