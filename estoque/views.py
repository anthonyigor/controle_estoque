from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView, DetailView

from .forms import EstoqueForm, EstoqueItensForm
from .models import EstoqueEntrada, EstoqueSaida, EstoqueItens, Produto, Estoque


class EstoqueEntradaList(TemplateView):
    template_name = 'estoque_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = EstoqueEntrada.objects.all()
        context['titulo'] = 'Entrada'
        context['url_add'] = 'estoque:estoque_entrada_add'
        return context



class EstoqueDetail(DetailView):
    model = Estoque
    template_name = 'estoque_detail.html'


def baixa_estoque(form):
    # pega todos os produtos adicionados no form
    produtos = form.estoques.all()

    # para cada item adicionado, o estoque é atualizado conforme o saldo atual
    for item in produtos:
        produto = Produto.objects.get(pk=item.produto.pk)
        produto.estoque = item.saldo
        produto.save()
    print('Estoque atualizado!')


def estoque_add(request, template_name, movimento, url):
    estoque_form = Estoque()

    '''cria a fábrica de forms inline
    param: model, inline_model, form em que serão salvos os dados '''
    item_estoque_formset = inlineformset_factory(
        Estoque,
        EstoqueItens,
        form=EstoqueItensForm,
        extra=0,
        can_delete=False,
        min_num=1,
        validate_min=True,
    )
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque_form, prefix='main')
        formset = item_estoque_formset(request.POST, instance=estoque_form, prefix='estoque')
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.funcionario = request.user
            form.movimento = movimento
            form.save()
            formset.save()
            baixa_estoque(form)
            return {'pk': form.pk}
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')
    context = {
        'form': form,
        'formset': formset,
    }
    return context


@login_required
def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    movimento = 'e'
    url = 'estoque:estoque_detail'
    context = estoque_add(request, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)


class EstoqueSaidaList(TemplateView):
    template_name = 'estoque_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = EstoqueSaida.objects.all()
        context['titulo'] = 'Saída'
        context['url_add'] = 'estoque:estoque_saida_add'
        return context


@login_required
def estoque_saida_add(request):
    template_name = 'estoque_saida_form.html'
    movimento = 's'
    url = 'estoque:estoque_detail'
    context = estoque_add(request, template_name, movimento, url)
    if context.get('pk'):
        return HttpResponseRedirect(resolve_url(url, context.get('pk')))
    return render(request, template_name, context)
