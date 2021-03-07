from django.urls import path, include
from api import views as api_views


app_name = "api"


urlpatterns = [
    path("<str:UF>/cidades/<str:city_name>", api_views.get_cidades_by_estado, name="cidade_by_estado"),
    path("imoveis/<str:UF>/<str:city_name>", api_views.get_imoveis, name="getImoveis")
]