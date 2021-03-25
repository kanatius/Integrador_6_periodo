from django.test import TestCase
from imovel.models import Cidade

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
        Cidade.objects.create(id=5, nome="Pau dos Ferros", estado_sigla="RN", estado="Rio Grande do Norte")
        
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