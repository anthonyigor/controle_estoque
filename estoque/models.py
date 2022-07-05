from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from produto.models import Produto
from django.urls import reverse_lazy

MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saída'),
)


class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE)
    nf = models.PositiveIntegerField('Nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.pk} - {self.nf} - {self.created.strftime("%d/%m/%Y")}'

    def nf_formated(self):
        return str(self.nf).zfill(5)

    def get_absolute_url(self):
        return reverse_lazy('estoque:estoque_entrada_detail', kwargs={'pk': self.pk})

class EstoqueItens(models.Model):
    estoque = models.ForeignKey(Estoque, on_delete=models.CASCADE, related_name='estoques')
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField()

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.pk}-{self.estoque}-{self.produto}'
