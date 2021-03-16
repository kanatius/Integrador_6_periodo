from django.db import models
from accounts.models import Usuario
from core.utils import removeAccentsOfString
# Create your models here.
from django.core.files.storage import default_storage
from integrador_6_periodo.settings import IMOVEIS_IMAGENS_DIR
import os

class Cidade(models.Model):

    nome = models.CharField(max_length=255)
    nome_sem_acentos = models.CharField(max_length=255)
    estado_sigla = models.CharField(max_length=2)
    estado = models.CharField(max_length=255)
    estado_sem_acentos = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):

        try:
            cidade = Cidade.objects.get(nome=self.nome, estado_sigla=self.estado_sigla)
        except:
            #salva somente se não houver uma cidade com aquele nome e estado
            self.nome_sem_acentos = removeAccentsOfString(self.nome)
            self.estado_sem_acentos = removeAccentsOfString(self.estado)
            super(Cidade, self).save(*args, **kwargs)


class Imovel(models.Model):

    TIPO_CHOICES = (
        ("C", "Casa"),
        ("A", "Apartamento"),
        ("S", "Sobrado"),
        ("K", "Kitnet"),
        ("E", "Edícula"),
        ("F", "Flat"),
    )
    STATUS_CHOICES = (
        ("D", "Disponível"),
        ("A", "Alugado"),
    )

    descricao = models.CharField(max_length=500, verbose_name="Descrição do seu imovel")
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES, default="C")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="D")
    valor_mensal = models.IntegerField()
    proprietario = models.ForeignKey(Usuario, default=2, blank=False, null=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Imovel"
        verbose_name_plural = "Imoveis"

    def __str__(self):
        return  str(self.id) + " - " + self.tipo

    def delete(self):

        imagens = self.imagens.all()

        for img in imagens:
            img.delete()
        
        super(Imovel, self).delete()


class ImovelImagem(models.Model):

    uri_arquivo = models.ImageField(upload_to=IMOVEIS_IMAGENS_DIR)
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE, related_name="imagens")

    class Meta:
        verbose_name = "Imovel imagem"
        verbose_name_plural = "Imovel imagens"

    def delete(self):
        os.remove(self.uri_arquivo.path) #remove arquivo da pasta
        super(ImovelImagem, self).delete()


class Endereco(models.Model):
    
    logradouro = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.IntegerField(null=True, blank=True, verbose_name="Número")
    ponto_de_referencia = models.CharField(max_length=255, null=True, blank=True)
    imovel = models.OneToOneField(Imovel, on_delete=models.CASCADE)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.bairro
