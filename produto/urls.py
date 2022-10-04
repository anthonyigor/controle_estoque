from django.urls import path

import produto.views as v

app_name = 'produto'

urlpatterns = [
    path('', v.ProductList.as_view(), name='product_list'),
    path('<int:pk>/', v.product_detail, name='product_detail'),
    path('add/', v.ProductCreate.as_view(), name='product_add'),
    path('<int:pk>/edit', v.ProductUpdate.as_view(), name='product_edit'),
    path('<int:pk>/json/', v.product_json, name='product_json'),
]
