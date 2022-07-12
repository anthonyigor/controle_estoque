from django.urls import path
import estoque.views as v

app_name = 'estoque'

urlpatterns = [
    path('', v.EstoqueEntradaList.as_view(), name='estoque_entrada_list'),
    path('<int:pk>/', v.estoque_entrada_detail, name='estoque_entrada_detail'),
    path('add/', v.estoque_entrada_add, name='estoque_entrada_add'),
    path('saida/', v.EstoqueSaidaList.as_view(), name='estoque_saida_list'),
    path('saida/<int:pk>/', v.estoque_saida_detail, name='estoque_saida_detail'),
]
