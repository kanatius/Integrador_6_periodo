from django.db import transaction
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from imovel.forms import ImovelForm, ImagemFormSet, EnderecoFormSet
from imovel.models import Imovel, ImovelImagem, Cidade
from django.shortcuts import render, redirect, HttpResponseRedirect
from api.serializers import ImovelSerializer
from django.core.mail import send_mail
from integrador_6_periodo.settings import EMAIL_HOST_USER
from django.contrib import messages


# Create your views here.

class CriarImovel(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Imovel
    form_class = ImovelForm
    template_name = 'imovel/cadastrar_imovel.html'
    success_url = reverse_lazy('core:index')

    def get(self, request, *args, **kwargs):

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = ImagemFormSet()
        formsetE = EnderecoFormSet()

        return self.render_to_response(
            self.get_context_data(form=form, formset=formset, formsetE=formsetE))

    def post(self, request, *args, **kwargs):
        cidade = None
        self.object = None

        form_class = self.get_form_class()
        form = self.get_form(form_class)

        formset = ImagemFormSet(self.request.POST, self.request.FILES)
        formsetE = EnderecoFormSet(self.request.POST)

        cidade = request.POST.get("cidade")
        estado = request.POST.get("estado")
        cidadeE = Cidade.objects.get(nome=cidade, estado_sigla=estado)

        if form.is_valid() and formset.is_valid() and formsetE.is_valid():

            form.instance.proprietario = self.request.user
            self.object = form.save()

            endereco = formsetE.save(commit=False)
            for e in endereco:
                e.imovel = self.object
                e.cidade = cidadeE
                e.save()

            media = formset.save(commit=False)
            for img in media:
                img.imovel = self.object
                img.save()
            return self.form_valid(form, formset, formsetE)
        else:
            return self.form_invalid(form, formset, formsetE)

    def form_valid(self, form, formset, formsetE):
        messages.success(self.request,'Imóvel cadastrado com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset, formsetE):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset, formsetE=formsetE))


def detalhes_page(request, id_imovel):
    imovel = None

    try:
        imovel = Imovel.objects.get(id=id_imovel)
    except:
        pass

    if imovel is None:
        return redirect("core:index")

    if imovel.status != "Disponível":
        return redirect("core:index")

    proprietario = imovel.proprietario

    imovel = ImovelSerializer(imovel, many=False).data

    if request.GET.get("success_message"):
        messages.success(request, request.GET.get("success_message"))

    return render(request, "imovel_detalhes.html", context={
        "imovel": imovel,
        "proprietario": proprietario,

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


class ListImovelUser(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Imovel
    template_name = 'imovel/lista_imoveis_user.html'

    def get_queryset(self):
        search = self.request.GET.get('search')
        queryset = None
        if search:
            queryset = Imovel.objects.filter(proprietario=self.request.user, tipo__icontains=search)
        else:
            queryset = Imovel.objects.filter(proprietario=self.request.user)
        return queryset


class UpdateImovelUser(UpdateView):
    model = Imovel
    fields = ('descricao', 'valor_mensal')
    template_name = 'imovel/editar_imovel.html'
    success_url = reverse_lazy('imovel:imoveis_user')

    def get_context_data(self, **kwargs):
        data = super(UpdateImovelUser, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ImagemFormSet(self.request.POST, self.request.FILES, instance=self.object)
            data['formsetE'] = EnderecoFormSet(self.request.POST, instance=self.object)
        else:
            data['formset'] = ImagemFormSet(instance=self.object)
            data['formsetE'] = EnderecoFormSet(instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        formsetE = context['formsetE']

        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid() and formsetE.is_valid():
                formsetE.instance = self.object
                formset.instance = self.object
                formset.save()
                formsetE.save()

        return super(UpdateImovelUser, self).form_valid(form)


class DeleteImovel(DeleteView):
    model = Imovel
    template_name = 'imovel/delete_imovel.html'
    success_url = reverse_lazy('imovel:imoveis_user')


