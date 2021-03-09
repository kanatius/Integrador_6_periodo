from django.urls import path
from core import views as core_views
from imovel.views import CriarImovel

app_name = 'imovel'

urlpatterns = [
    path('cadastrar_imovel/', CriarImovel.as_view(), name="cadastrarImovel")
]