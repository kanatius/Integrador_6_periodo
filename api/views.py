from django.shortcuts import render
from imovel.models import Cidade
from django.http import HttpResponse
from django.db.models import Q
from django.core import serializers

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