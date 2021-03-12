from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from imovel.models import Imovel, ImovelImagem, Endereco


class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = [
            'descricao',
            'tipo',
            'status',
            'valor_mensal'
        ]


class ImagemImovelForm(ModelForm):
    class Meta:
        model = ImovelImagem
        exclude = ['imovel']


class EnderecoImovelForm(ModelForm):
    class Meta:
        model = Endereco
        exclude = ['imovel']


ImagemFormSet = inlineformset_factory(Imovel, ImovelImagem, form=ImagemImovelForm)
EnderecoFormSet = inlineformset_factory(Imovel, Endereco, form=EnderecoImovelForm)
