from django.views.generic import CreateView

from imovel.forms import ImovelForm
from imovel.models import Imovel


class CriarImovel(CreateView):
    model = Imovel
    form_class = ImovelForm
