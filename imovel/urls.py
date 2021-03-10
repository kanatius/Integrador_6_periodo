from django.urls import path
from core import views as core_views
from imovel import views as imovel_views

app_name = 'imovel'

urlpatterns = [
    path("detalhes/<int:id_imovel>", imovel_views.detalhes_page)
]