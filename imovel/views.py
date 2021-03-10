from django.shortcuts import render, redirect
from .models import Imovel
from api.serializers import ImovelSerializer
# Create your views here.


def detalhes_page(request, id_imovel):

    imovel = None

    try:
        imovel = Imovel.objects.get(id=id_imovel)
    except:
        pass

    if imovel is None:
        return redirect(request, "core:index")

    proprietario = imovel.proprietario

    imovel = ImovelSerializer(imovel, many=False).data


    return render(request, "imovel_detalhes.html", context={
        "imovel" : imovel,
        "proprietario" : proprietario
    })