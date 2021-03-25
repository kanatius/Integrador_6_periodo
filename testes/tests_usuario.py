from django.test import TestCase
from accounts.models import Usuario
from django.db.models import Q
import unittest

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

    
    


