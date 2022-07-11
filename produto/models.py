from django.db import models
from django.urls import reverse_lazy


class Produto(models.Model):
    produto = models.CharField('Produto', max_length=100, unique=True)
    ncm = models.CharField('NCM', max_length=8)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque atual')
    estoque_minimo = models.PositiveIntegerField('Estoque mínimo', default=0)

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto

    def get_absolute_url(self):
        return reverse_lazy('produto:product_detail', kwargs={'pk': self.pk})

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }
