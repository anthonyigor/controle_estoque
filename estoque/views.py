from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView
from .models import EstoqueEntrada, EstoqueSaida, EstoqueItens, Produto, Estoque
from .forms import EstoqueForm, EstoqueItensForm
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect


class EstoqueEntradaList(TemplateView):
    template_name = 'estoque_entrada_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = EstoqueEntrada.objects.all()
        return context


def estoque_entrada_detail(request, pk):
    template_name = 'estoque_entrada_detail.html'
    obj = EstoqueEntrada.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def baixa_estoque(form):
    # pega todos os produtos adicionados no form
    produtos = form.estoques.all()

    # para cada item adicionado, o estoque é atualizado conforme o saldo atual
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
    print('Estoque atualizado!')


def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    estoque_form = Estoque()

    '''cria a fábrica de forms inline
    param: model, inline_model, form em que serão salvos os dados '''
    item_estoque_formset = inlineformset_factory(
        EstoqueEntrada,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        min_num=1,
        validate_min=True,
    )

    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(request.POST, instance=estoque_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save()
            formset.save()
            baixa_estoque(form)
            url = 'estoque:estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


class EstoqueSaidaList(TemplateView):
    template_name = 'estoque_saida_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = EstoqueSaida.objects.all()
        return context


def estoque_saida_detail(request, pk):
    template_name = 'estoque_saida_detail.html'
    obj = EstoqueSaida.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)
