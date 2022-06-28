from django.db import models


class Produto(models.Model):
    produto = models.CharField('Produto', max_length=100, unique=True)
    ncm = models.CharField('NCM', max_length=8)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque atual')
    estoque_minimo = models.PositiveIntegerField('Estoque mínimo', default=0)

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return produto
