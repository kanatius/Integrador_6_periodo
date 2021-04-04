from django.shortcuts import render
from imovel.models import Cidade, Imovel
from django.http import HttpResponse
from django.db.models import Q
from django.core import serializers
from .serializers import ImovelSerializer, CidadeSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, parser_classes, permission_classes
import json
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


offset = openapi.Parameter('offset', openapi.IN_QUERY, default=0, description="", type=openapi.TYPE_INTEGER)
limit= openapi.Parameter('limit', openapi.IN_QUERY, default=0, description="Limite de impressões retornadas", type=openapi.TYPE_INTEGER)



@swagger_auto_schema(method='GET',  manual_parameters=[offset, limit], responses={ 200 : CidadeSerializer})
@api_view(["GET"])
def get_cidades_by_estado(request, UF, city_name):

    if request.method == "GET":
        cidades = Cidade.objects.filter(estado_sigla__iexact=UF)

        cidades = cidades.filter((Q(nome__icontains=city_name) | Q(nome_sem_acentos__icontains=city_name)))

        if request.GET.get("offset"):
            offset = int(request.GET.get("offset"))
            cidades = cidades[offset:]
    
        if request.GET.get("limit"):
            limit = int(request.GET.get("limit"))
            cidades = cidades[:limit]

        data = CidadeSerializer(cidades, many=True).data
        data = json.dumps(data)
        return HttpResponse(data, content_type='application/json')


@swagger_auto_schema(method='GET', manual_parameters=[offset, limit], responses={ 200 : ImovelSerializer})
@api_view(["GET"])
def get_imoveis(request, UF, city_name):

    imoveis = Imovel.objects.filter(endereco__cidade__nome=city_name, endereco__cidade__estado_sigla=UF)

    # data = serializers.serialize("json", imoveis, use_natural_foreign_keys=True, use_natural_primary_keys=True)

    if request.GET.get("offset"):
        offset = int(request.GET.get("offset"))
        imoveis = imoveis[offset:]
    
    if request.GET.get("limit"):
        limit = int(request.GET.get("limit"))
        imoveis = imoveis[:limit]

    data = ImovelSerializer(imoveis, many=True).data

    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')

@swagger_auto_schema(method='GET',  manual_parameters=[offset, limit], responses={ 200 : ImovelSerializer})
@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def meusImoveis(request):

    imoveis = Imovel.objects.filter(proprietario=request.user)


    if request.GET.get("offset"):
        offset = int(request.GET.get("offset"))
        imoveis = imoveis[offset:]
    
    if request.GET.get("limit"):
        limit = int(request.GET.get("limit"))
        if limit > 0:
            imoveis = imoveis[:limit]


    data = ImovelSerializer(imoveis, many=True).data

    data = json.dumps(data)

    return HttpResponse(data, content_type='application/json')

@swagger_auto_schema(method='GET', responses={ 200 : ImovelSerializer})
@api_view(["GET"])
def getImovel(request, id):

    try:
        imovel = Imovel.objects.get(id=id)
        data = ImovelSerializer(imovel, many=False).data

        data = json.dumps(data)

        return HttpResponse(data, content_type='application/json')

    except:
        data = json.dumps(None)
        return HttpResponse(data, content_type='application/json')