from django.test import TestCase
from imovel.models import Cidade
from accounts.models import Usuario

class CidadeTestCase(TestCase):
    
    def setUp(self):
        Cidade.objects.create(nome="Alexandria", estado_sigla="RN", estado="Rio Grande do Norte")
        Cidade.objects.create(nome="Rafael Fernandes", estado_sigla="RN", estado="Rio Grande do Norte")
        Cidade.objects.create(nome="Brasília", estado_sigla="DF", estado="Distrito Federal")


    def test_two_cities_one_state(self):
        rn_cities_amount = Cidade.objects.filter(estado_sigla="RN").count()
        self.assertEqual(rn_cities_amount, 2)

    def test_two_cities_same_ones(self):
        city = Cidade(nome="Brasília", estado_sigla="DF", estado="Distrito Federal")
        city.save()
        brasilia_amount = Cidade.objects.filter(estado_sigla="DF").count()

        self.assertEqual(brasilia_amount, 1)

    def test_no_accents_city(self):

        brasilia = Cidade.objects.get(nome="Brasília", estado_sigla="DF")
        self.assertEquals(brasilia.nome_sem_acentos, "Brasilia")
    
    
    def test_no_accents_state(self):
        fortaleza = Cidade(nome="Fortaleza", estado_sigla="CE", estado="Ceará")
        fortaleza.save()

        state_no_accents = fortaleza.estado_sem_acentos

        fortaleza.delete()

        self.assertEquals(state_no_accents, "Ceara")


# class UsuarioTestCase(TestCase):

#     def test_create_user(self):
#         user = Usuario(email="teste@gmail.com", nome="Usuario", sobrenome="Teste", telefone="(11) 9 9999 8877", password="123123")
#         user.save()
        
#         exc = False

#         try:
#             usuario = Usuario.objects.get(email="teste@gamil.com")
#         except:
#            exc = True

#         self.assertFalse(exc) 
