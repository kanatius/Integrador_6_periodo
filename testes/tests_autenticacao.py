import unittest

from django.test import Client
from django.test import TestCase
from integrador_6_periodo.settings import BASE_DIR
import os
from accounts.models import Usuario
from imovel.models import Imovel, ImovelImagem
from django.core.files.uploadedfile import SimpleUploadedFile


class AutenticacaoTestFuncional(TestCase):

    @classmethod
    def setUpTestData(cls):
        Usuario.objects._create_user(id=1, email="teste@gmail.com", nome="Usuario", sobrenome="Teste",
                                     telefone="(11) 9 9999 8877", password="senha123")
        Imovel.objects.create(id=1, descricao="3 quartos, sala e cozinha", tipo="Apartamento", status="Disponível",
                              valor_mensal=500, proprietario=Usuario.objects.get(id=1))

    def setUp(self):
        ImovelImagem.objects.all().delete()

    def test_login(self):
        c = Client()
        #login()retorna True se as credenciais foram aceitas e o login foi bem-sucedido.
        self.assertTrue(c.login(username='teste@gmail.com', password='senha123'))

    def test_login_senha_invalida(self):
        c = Client()
        #login()retorna False se as credenciais não foram aceitas e o login foi bem-sucedido.
        self.assertFalse(c.login(username='teste@gmail.com', password='senha1233'))

    def test_max_image(self):
        imovel = Imovel.objects.get(id=1)
        imgPath = os.path.join(BASE_DIR,"testes\\img_teste\\quarto-de-casal.jpeg")
        for i in range(5):
            ii = ImovelImagem(imovel=imovel, uri_arquivo=SimpleUploadedFile(name='quarto-de-casal.jpeg', content=open(imgPath, 'rb').read()))
            ii.save()

        self.assertTrue(ImovelImagem.objects.filter(imovel=imovel).count(), 5)

    def test_superior_image(self):
        imovel = Imovel.objects.get(id=1)
        imgPath = os.path.join(BASE_DIR,"testes\\img_teste\\quarto-de-casal.jpeg")
        for i in range(6):
            ii = ImovelImagem(imovel=imovel, uri_arquivo=SimpleUploadedFile(name='quarto-de-casal.jpeg', content=open(imgPath, 'rb').read()))
            ii.save()

        self.assertTrue(ImovelImagem.objects.filter(imovel=imovel).count(), 5)

    @unittest.expectedFailure
    def test_image_sem_imovel(self):
        imgPath = os.path.join(BASE_DIR,"testes\\img_teste\\quarto-de-casal.jpeg")
        ii = ImovelImagem(imovel=None, uri_arquivo=SimpleUploadedFile(name='quarto-de-casal.jpeg', content=open(imgPath, 'rb').read()))
        ii.save()

    def test_clean_img(self):
        ImovelImagem.objects.all().delete()


