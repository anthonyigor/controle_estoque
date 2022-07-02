from django.contrib import admin
from produto.models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'ncm', 'preco', 'estoque', 'estoque_minimo')
    search_fields = ('produto',)
