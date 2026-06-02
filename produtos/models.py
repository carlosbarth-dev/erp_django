from django.db import models

class Produto(models.Model):
    class UnidadeMedida(models.TextChoices):
        UNIDADE = 'UN', 'Unidade'
        METRO_QUADRADO = 'M2', 'Metro quadrado'
        METRO_LINEAR = 'ML', 'Metro linear'
        METRO_CUBICO = 'M3', 'Metro cubico'

    codigo = models.CharField(max_length=30, unique=True)
    nome = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    unidade_medida = models.CharField(
        max_length=2,
        choices=UnidadeMedida.choices,
    )
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.codigo} - {self.nome}'
    
    class Meta:
        ordering = ['codigo']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
