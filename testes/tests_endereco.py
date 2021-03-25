from django.test import TestCase
from imovel.models import Cidade, Endereco, Imovel

class EnderecoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cidade.objects.create(id=5, nome="Pau dos Ferros", estado_sigla="RN", estado="Rio Grande do Sul")
        Imovel.objects.create(id=1, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario)
    
    def setUp(self):
        Endereco.objects.all().delete()