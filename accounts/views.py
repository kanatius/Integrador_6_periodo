from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from accounts.forms import CreateUserForm
from imovel.models import Imovel
# ------- REDIRECT/RESPONSE -------#
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect, HttpResponseRedirect
# ------- REDIRECT/RESPONSE -------#
# ------- RELATÓRIO -------#
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
# ------- RELATÓRIO -------#

class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('core:index')


class Cadastro(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/cadastro.html'


def gerar_relatorio(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(request, "/")

    usuario = request.user

    imoveis = Imovel.objects.filter(proprietario = usuario)

    qtd_imoveis = imoveis.count()
    qtd_imoveis_diponíveis = 0
    qtd_imoveis_alugados = 0
    val_recebido_por_mes = 0
    val_n_recebido_por_mes = 0
    total_val_im = 0

    for imovel in imoveis:
        if imovel.status == "Disponível":
            qtd_imoveis_diponíveis += 1
            val_n_recebido_por_mes += imovel.valor_mensal
        elif imovel.status == "Alugado":
            qtd_imoveis_alugados += 1
            val_recebido_por_mes += imovel.valor_mensal

    template = get_template("relatorio.html")
    html  = template.render({
        "usuario" : request.user,
        "qtd_im_disp" : qtd_imoveis_diponíveis,
        "qtd_im_alug" : qtd_imoveis_alugados,
        "val_receb_mes" : val_recebido_por_mes,
        "val_n_receb_mes" : val_n_recebido_por_mes,
        })
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)

    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')


    return HttpResponseRedirect(request, "/")