from .models import Produto
from .forms import ProdutoForm
from django.views.generic import TemplateView, CreateView, UpdateView
from django.shortcuts import render
from django.http import JsonResponse


class ProductList(TemplateView):
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


class ProductAdd(TemplateView):
    template_name = 'produto_form.html'


class ProductCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProductUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


def product_json(request, pk):
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})
