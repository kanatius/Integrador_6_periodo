from django.urls import path
from core import views as core_views
from imovel.views import CriarImovel
from imovel import views as imovel_views
from django.urls import include

app_name = 'imovel'

urlpatterns = [
    path('cadastrar_imovel/', CriarImovel.as_view(), name="cadastrarImovel"),
    path("detalhes/<int:id_imovel>", imovel_views.detalhes_page, name="imovel_detalhes"),
    path("enviarEmailProp/<int:id_imovel>", imovel_views.enviar_email_prop, name="enviar_email_prop")
]