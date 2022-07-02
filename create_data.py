import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

import string
from random import choice, random, randint
from produto.models import Produto


class Utils:
    #cria métodos genéricos

    '''método para gerar números aleatórios
    max_lenght = Quantidade de dígitos que o número aleatório deve ter'''
    @staticmethod
    def gen_digits(max_lenght):
        return str(''.join(choice(string.digits) for i in range(max_lenght)))


class ProdutoClass:
    @staticmethod
    def criar_produtos(produtos):
         Produto.objects.all().delete()
         aux_list = []

         #varre a lista de produtos e gera dados aleatórios para cada um
         for produto in produtos:
             data = dict(
                 produto=produto,
                 ncm=Utils.gen_digits(8),
                 preco=random() * randint(10, 50),
                 estoque=randint(1, 300),
             )
             obj = Produto(**data)
             aux_list.append(obj)

         #Salva os dados gerados
         Produto.objects.bulk_create(aux_list)


produtos = (
    'Amortecedor Titan 150 Cofap',
    'Kit CCP XT660 KMC',
    'Oleo Lubrax 20w50',
    'Oleo Motul 10w40',
    'Porta Corrente Titan 150 14/ Stlu',
    'Pneu 90/90-18 Vipal ST300',
)

ProdutoClass.criar_produtos(produtos)
