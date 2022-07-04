from django.urls import path
import produto.views as v


app_name = 'produto'

urlpatterns = [
    path('', v.product_list.as_view(), name='product_list'),
    path('<int:pk>/', v.product_detail, name='product_detail'),
]
