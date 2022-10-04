from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView

from .forms import ProdutoForm
from .models import Produto


class ProductList(ListView):
    model = Produto
    template_name = 'product_list.html'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        search = self.request.GET.get('search')
        if search:
            objects_list = Produto.objects.filter(produto__icontains=search)
            return objects_list

        objects_list = Produto.objects.all()
        return objects_list


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
