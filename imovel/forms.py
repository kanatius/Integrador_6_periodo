from django.forms import ModelForm, forms
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
        exclude = ['imovel', 'cidade']

    # def __init__(self, *args, **kwargs):
    #     super(EnderecoImovelForm, self).__init__(*args, **kwargs)
    #     self.fields['extra_field'] = forms.TextField()


ImagemFormSet = inlineformset_factory(Imovel, ImovelImagem, form=ImagemImovelForm)
EnderecoFormSet = inlineformset_factory(Imovel, Endereco, form=EnderecoImovelForm, extra=1)
