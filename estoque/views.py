from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Estoque


class EstoqueEntradaList(TemplateView):
    template_name = 'estoque_entrada_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Estoque.objects.filter(movimento='e')
        return context


def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    obj = Estoque.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)
