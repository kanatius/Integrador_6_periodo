from rest_framework import serializers
from imovel.models import Imovel, Endereco, Cidade, ImovelImagem
from integrador_6_periodo.settings import IMOVEIS_IMAGENS_DIR, STATIC_URL, MEDIA_ROOT


class CidadeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cidade
        fields = ('id', 'nome', 'estado_sigla', 'estado')

class EnderecoSerializer(serializers.ModelSerializer):
    
    cidade = CidadeSerializer(read_only=True)

    class Meta:
        model = Endereco
        fields = ('id', 'logradouro', 'bairro', 'numero', 'ponto_de_referencia', 'cidade')

class ImagemSerializer(serializers.ModelSerializer):

    link = serializers.SerializerMethodField('get_image_link')

    class Meta:
        model = ImovelImagem
        fields = ('id', 'link')

    def get_image_link(self, instance):
        return STATIC_URL +  instance.uri_arquivo.name

class ImovelSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    
    imagens = ImagemSerializer(many=True)
    
    class Meta:
        model = Imovel
        fields = ('id', 'tipo', 'descricao', 'status', 'valor_mensal', 'endereco', 'imagens')