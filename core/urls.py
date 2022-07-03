from django.urls import path
import core.views as v

app_name = 'core'

urlpatterns = [
    path('', v.index.as_view(), name='index'),
]
