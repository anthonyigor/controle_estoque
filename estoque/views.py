#from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Estoque


class EstoqueEntradaList(TemplateView):
    template_name = 'estoque_entrada_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Estoque.objects.filter(movimento='e')
        return context
