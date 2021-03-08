from django.forms import ModelForm

from imovel.models import Imovel


class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fildes = '__all__'