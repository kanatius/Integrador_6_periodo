from django.db import models
from accounts.models import Usuario
from core.utils import removeAccentsOfString
# Create your models here.
from django.core.files.storage import default_storage

class Cidade(models.Model):

    nome = models.CharField(max_length=255)
    nome_sem_acentos = models.CharField(max_length=255)
    estado_sigla = models.CharField(max_length=2)
    estado = models.CharField(max_length=255)
    estado_sem_acentos = models.CharField(max_length=255)
    

    def save(self, *args, **kwargs):
        self.nome_sem_acentos = removeAccentsOfString(self.nome)
        self.estado_sem_acentos = removeAccentsOfString(self.estado)
        super(Cidade, self).save(*args, **kwargs)


class Imovel(models.Model):

    descricao = models.CharField(max_length=500)
    tipo = models.CharField(max_length=55)
    status = models.CharField(max_length=55)
    valor_mensal = models.IntegerField()

    def delete(self):

        imagens = self.imagens.all()

        for img in imagens:
            img.delete()
        
        super(Imovel, self).delete()

class ImovelImagem(models.Model):

    uri_arquivo = models.FileField()
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name="imagens")

    def delete(self):
        default_storage.delete(str(self.uri_arquivo)) #remove arquivo da pasta
        super(ImovelImagem, self).delete()


class Endereco(models.Model):
    
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.IntegerField(null=True, blank=True)
    ponto_de_referencia = models.CharField(max_length=55, null=True, blank=True)
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)


