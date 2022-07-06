from django.shortcuts import render, resolve_url
from django.views.generic import TemplateView
from .models import Estoque, EstoqueItens
from .forms import EstoqueForm, EstoqueItensForm
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect


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


def estoque_entrada_add(request):
    template_name = 'estoque_entrada_form.html'
    estoque_form = Estoque()
    item_estoque_formset = inlineformset_factory(
        Estoque,
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
            url = 'estoque_entrada_detail'
            return HttpResponseRedirect(resolve_url(url, form.pk))
    else:
        form = EstoqueForm(instance=estoque_form, prefix='main')
        formset = item_estoque_formset(instance=estoque_form, prefix='estoque')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)
