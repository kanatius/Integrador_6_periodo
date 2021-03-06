from django.urls import path
from core.views import index_page
from core import views as core_views

app_name = "core"

urlpatterns = [
    path("", index_page.as_view(), name="index"),

    path("imoveis", core_views.imoveis_page, name="imoveis_page"),
]