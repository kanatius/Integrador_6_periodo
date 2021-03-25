from django.test import TestCase
from imovel.models import Cidade, Imovel
from accounts.models import Usuario

class ImovelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cidade.objects.create(id=1, nome="Alexandria", estado_sigla="RN", estado="Rio Grande do Norte")
        Usuario.objects._create_user(id=1, email="teste1@gmail.com", nome="Usuario", sobrenome="Teste", telefone="(11) 9 9999 8877", password="asdasda213")
        Usuario.objects._create_user(id=2, email="teste2@gmail.com", nome="Usuario2", sobrenome="Teste2", telefone="(11) 9 9992 8877", password="asda23a213")
        cls.proprietario = Usuario.objects.get(email="teste1@gmail.com")
        cls.proprietario2 = Usuario.objects.get(email="teste2@gmail.com")


    def setUp(self):
        Imovel.objects.all().delete()


    def test_create_Imovel(self):
        
        imovel = Imovel(id=1, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario)
        imovel.save()

        imovel_ = Imovel.objects.get(id=1)

        self.assertEquals(imovel, imovel_)


    def test_2_imoveis_1_prop(self):
        
        Imovel.objects.create(id=1, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario)
        Imovel.objects.create(id=2, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario)

        amount = Imovel.objects.filter(proprietario = ImovelTestCase.proprietario).count()

        self.assertEquals(amount, 2)

    #testa se os imóveis estão sendo salvos para o proprietatio certo
    def test_diff_props(self):

        Imovel.objects.create(id=1, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario)
        Imovel.objects.create(id=2, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario)
        
        #proprietario 2
        Imovel.objects.create(id=3, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario2)

        amount = Imovel.objects.filter(proprietario = ImovelTestCase.proprietario).count()

        self.assertEquals(amount, 2)