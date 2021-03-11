from django.urls import path
from core import views as core_views
from imovel import views as imovel_views

app_name = 'imovel'

urlpatterns = [
    path("detalhes/<int:id_imovel>", imovel_views.detalhes_page, name="imovel_detalhes"),
    path("enviarEmailProp/<int:id_imovel>", imovel_views.enviar_email_prop, name="enviar_email_prop")
]