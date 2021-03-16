from django.test import TestCase
import unittest
from imovel.models import Cidade, Endereco, Imovel, ImovelImagem
from accounts.models import Usuario
from django.db.models import Q

class UsuarioTestCase(TestCase):

    def setUp(self):
        Usuario.objects.all().delete()

    #teste criação de usuario
    def test_create_user(self):
        usuario = Usuario(email="teste@gmail.com", nome="Usuario", sobrenome="Teste", telefone="(11) 9 9999 8877", password="123123")
        usuario.save()

        try:
            usuario = Usuario.objects.get(email="teste@gmail.com")
        except:
           self.fail("Usuário Não criado")
           return
        
        self.assertNotEquals(usuario, None)
    
    #teste se a senha foi criptografada
    def test_password_is_encrypted(self):

        password = "123123123"
        
        try:
            Usuario.objects._create_user(email="teste@gmail.com", nome="Usuario", sobrenome="Teste", telefone="(11) 9 9999 8877", password=password)    
        except:
            self.fail("Erro ao criar usuário")
            return
        
        usuario = Usuario.objects.get(email="teste@gmail.com")
        
        self.assertNotEquals(password, usuario.password)
    
    #teste para cadastro de usuario com e-mail único
    @unittest.expectedFailure
    def test_two_users_same_email(self):

        try:
            Usuario.objects._create_user(email="teste2@gmail.com", nome="Usuario", sobrenome="Teste", telefone="(11) 9 9999 8877", password="asdasda213")    
            Usuario.objects._create_user(email="teste2@gmail.com", nome="Usuario2", sobrenome="Teste2", telefone="(11) 9 9999 8827", password="qweewe12")
        except:
            self.fail("Só pode haver um usuário com o mesmo e-mail")


class CidadeTestCase(TestCase):
    
    #beforeAll
    @classmethod
    def setUpTestData(cls):
        Cidade.objects.create(id=1, nome="Alexandria", estado_sigla="RN", estado="Rio Grande do Norte")
        Cidade.objects.create(id=2, nome="Rafael Fernandes", estado_sigla="RN", estado="Rio Grande do Norte")
        Cidade.objects.create(id=3, nome="Brasília", estado_sigla="DF", estado="Distrito Federal")

    def setUp(self):
        Cidade.objects.filter(id__gte=4).delete()

    #testar cidades em diferentes estados
    def test_two_cities_one_state(self):
        rn_cities_amount = Cidade.objects.filter(estado_sigla="RN").count()
        self.assertEqual(rn_cities_amount, 2)

    #teste de 2 cidades com o mesmo nome e estado
    def test_two_cities_same_ones(self):
        Cidade.objects.create(id=4, nome="Pau dos Ferros", estado_sigla="RN", estado="Rio Grande do Norte")
        Cidade.objects.create(id=5, nome="Pau dos Ferros", estado_sigla="RN", estado="Rio Grande do Sul")
        
        pdf_amount = Cidade.objects.filter(nome="Pau dos Ferros").count()

        self.assertEqual(pdf_amount, 1)

    #teste de 2 cidades com o mesmo nome e estado diferente
    def test_two_cities_same_name(self):
        Cidade.objects.create(id=4, nome="Pau dos Ferros", estado_sigla="RN", estado="Rio Grande do Norte")
        Cidade.objects.create(id=5, nome="Pau dos Ferros", estado_sigla="RS", estado="Rio Grande do Sul")

        pdf_amount = Cidade.objects.filter(nome="Pau dos Ferros").count()

        self.assertEqual(pdf_amount, 2)

    #testa se a variável nome_sem_acentos foi definida com sucesso
    def test_no_accents_city(self):

        brasilia = Cidade.objects.get(nome="Brasília", estado_sigla="DF")
        self.assertEquals(brasilia.nome_sem_acentos, "Brasilia")
    
    
    def test_no_accents_state(self):
        fortaleza = Cidade(id=4, nome="Fortaleza", estado_sigla="CE", estado="Ceará", estado_sem_acentos="Cearáááá")
    
        fortaleza.save()

        state_no_accents = fortaleza.estado_sem_acentos

        self.assertEquals(state_no_accents, "Ceara")

        
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


class EnderecoTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cidade.objects.create(id=5, nome="Pau dos Ferros", estado_sigla="RN", estado="Rio Grande do Sul")
        Imovel.objects.create(id=1, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível", valor_mensal=500, proprietario=ImovelTestCase.proprietario)
    
    def setUp(self):
        Endereco.objects.all().delete()

    
    


