from unicodedata import normalize
import requests
from django.apps import apps


def removeAccentsOfString(txt):
  return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def addRnCitiesFromIBGE():

    Cidade = apps.get_model('imovel','Cidade')

    estados = {
        'AC' : 'Acre',
        'AL' : 'Alagoas',
        'AP' : 'Amapá',
        'AM' : 'Amazonas',
        'BA' : 'Bahia',
        'CE' : 'Ceará',
        'DF' : 'Distrito Federal',
        'ES' : 'Espirito Santo',
        'GO' : 'Goiás',
        'MA' : 'Maranhão',
        'MS' : 'Mato Grosso do Sul',
        'MT' : 'Mato Grosso',
        'MG' : 'Minas Gerais',
        'PA' : 'Pará',
        'PB' : 'Paraíba',
        'PR' : 'Paraná',
        'PE' : 'Pernambuco',
        'PI' : 'Piauí',
        'RJ' : 'Rio de Janeiro',
        'RN' : 'Rio Grande do Norte',
        'RS' : 'Rio Grande do Sul',
        'RO' : 'Rondônia',
        'RR' : 'Roraima',
        'SC' : 'Santa Catarina',
        'SP' : 'São Paulo',
        'SE' : 'Sergipe',
        'TO' : 'Tocantins',
    }


    for sigla in estados:
        cidades = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/" + sigla + "/distritos").json()
        
        for cidade in cidades:

            try:
                Cidade.objects.get(nome=cidade["nome"], estado_sigla=sigla)    
            except:
                print("Saving: " + cidade["nome"])
                cidade_model = Cidade(nome=cidade["nome"], estado=estados[sigla], estado_sigla=sigla)
                cidade_model.save()
    
    