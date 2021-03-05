from django.shortcuts import render, redirect
from imovel.models import Cidade

# Create your views here.
def index_page(request):
    return render(request, "index.html")

def imoveis_page(request):

    if request.method == "GET":
        cidade = None

        try:
            cidade = Cidade.objects.get(nome=request.GET["cidade"], estado_sigla=request.GET["estado"])
        except:
            return redirect(request, "core:index")
            pass

        return render(request, "listagem_imoveis.html", context = {"cidade" : cidade})