from .models import Produto
from django.views.generic import TemplateView


class product_list(TemplateView):
    template_name = 'product_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Produto.objects.all()
        return context
