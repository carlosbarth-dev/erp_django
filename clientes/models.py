from django.db import models

class Cliente(models.Model):
    class TipoPessoa(models.TextChoices):
        FISICA = 'FISICA', 'Pessoa Fisica'
        JURIDICA = 'JURIDICA', 'Pessoa Juridica'

    tipo_pessoa = models.CharField(
        max_length=10,
        choices=TipoPessoa.choices,

    )
    nome = models.CharField(max_length=150)
    documento = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    endereco = models.TextField(blank=True)
    ativo = models.BooleanField(default=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome
