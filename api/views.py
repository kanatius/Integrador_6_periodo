from django.shortcuts import render
from imovel.models import Cidade, Imovel
from django.http import HttpResponse
from django.db.models import Q
from django.core import serializers
from .serializers import ImovelSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import json


# Create your views here.
def get_cidades_by_estado(request, UF, city_name):

    if request.method == "GET":
        cidades = Cidade.objects.filter(estado_sigla__iexact=UF)

        cidades = cidades.filter((Q(nome__icontains=city_name) | Q(nome_sem_acentos__icontains=city_name)))

        data = ""

        if request.GET.get("limit"):
            limit = int(request.GET.get("limit"))
            data = serializers.serialize("json", cidades[:limit])
        else:
            data = serializers.serialize("json", cidades)

        return HttpResponse(data, content_type='application/json')


def get_imoveis(request, UF, city_name):

    imoveis = Imovel.objects.filter(endereco__cidade__nome=city_name, endereco__cidade__estado_sigla=UF)

    # data = serializers.serialize("json", imoveis, use_natural_foreign_keys=True, use_natural_primary_keys=True)

    data = ImovelSerializer(imoveis, many=True).data

    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')