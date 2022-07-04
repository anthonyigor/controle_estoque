from .models import Produto
from django.views.generic import TemplateView
from django.shortcuts import render


class product_list(TemplateView):
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Produto.objects.all()
        return context


def product_detail(request, pk):
    template_name = 'product_detail.html'
    obj = Produto.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)
