from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Imovel
from api.serializers import ImovelSerializer
from django.core.mail import send_mail
from integrador_6_periodo.settings import EMAIL_HOST_USER
from django.contrib import messages
# Create your views here.


def detalhes_page(request, id_imovel):

    imovel = None

    try:
        imovel = Imovel.objects.get(id=id_imovel)
    except:
        pass

    if imovel is None:
        return redirect("core:index")

    proprietario = imovel.proprietario

    imovel = ImovelSerializer(imovel, many=False).data

    if request.GET.get("success_message"):
        messages.success(request, request.GET.get("success_message"))

    return render(request, "imovel_detalhes.html", context={
        "imovel" : imovel,
        "proprietario" : proprietario
    })

def enviar_email_prop(request, id_imovel):

    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")

    if request.method == "POST":
        imovel = Imovel.objects.get(id=id_imovel)

        mens = "De: " + request.user.getFullName() + "\n"

        mens += "----------------------------------\n\n"

        mens += request.POST.get("texto-mens") + "\n\n"

        mens += "----------------------------------\n"


        send_mail(
                'Alguém se interessou por seu imóvel',
                mens,
                EMAIL_HOST_USER,
                [imovel.proprietario.email],
                fail_silently=False,
            )
        success_message = "Email enviado com sucesso!"

        link_return = "/imovel/detalhes/" + str(imovel.id) + "?success_message=" + success_message + "#div-email"

        return HttpResponseRedirect(link_return)