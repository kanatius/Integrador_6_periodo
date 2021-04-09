from django.test import TestCase
import unittest
from imovel.models import Cidade, Endereco, Imovel, Usuario


class EnderecoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cidade.objects.create(id=5, nome="Pau dos Ferros", estado_sigla="RN", estado="Rio Grande do Sul")
        Usuario.objects._create_user(id=1, email="teste1@gmail.com", nome="Usuario", sobrenome="Teste",
                                     telefone="(11) 9 9999 8877", password="asdasda213")
        Imovel.objects.create(id=1, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível",
                              valor_mensal=500, proprietario=Usuario.objects.get(id=1))

    def setUp(self):
        Endereco.objects.all().delete()

    def test_create_Endereco(self):
        imovel = Imovel.objects.get(id=1)
        cidade = Cidade.objects.get(id=5)
        endereco = Endereco.objects.create(id=1, logradouro=1, bairro="centro", numero=22, ponto_de_referencia="Igreja",
                                           imovel=imovel, cidade=cidade)

        self.assertNotEqual(endereco, None)

    @unittest.expectedFailure
    def test_endereco_sem_imovel(self):
        cidade = Cidade.objects.get(id=5)
        endereco = Endereco.objects.create(id=1, logradouro=1, bairro="centro", numero=22, ponto_de_referencia="Igreja",
                                           imovel=None, cidade=cidade)

    @unittest.expectedFailure
    def test_endereco_sem_cidade(self):
        imovel = Imovel.objects.get(id=1)
        endereco = Endereco.objects.create(id=1, logradouro=1, bairro="centro", numero=22, ponto_de_referencia="Igreja",
                                           imovel=imovel, cidade=None)
