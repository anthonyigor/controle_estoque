from django.contrib import admin
from .models import EstoqueEntrada, EstoqueSaida, EstoqueItens


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nf', 'funcionario')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
    inlines = (EstoqueItensInline,)


@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nf', 'funcionario')
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'
    inlines = (EstoqueItensInline,)
