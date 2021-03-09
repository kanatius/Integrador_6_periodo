from django.http import HttpResponseRedirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from imovel.forms import ImovelForm, ImagemFormSet
from imovel.models import Imovel, ImovelImagem


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
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):

        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = ImagemFormSet(self.request.POST, self.request.FILES)

        if form.is_valid() and formset.is_valid():
            form.instance.proprietario = self.request.user
            self.object = form.save()
            media = formset.save(commit=False)
            for img in media:
                img.imovel = self.object
                img.save()
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(form=form, formset=formset))


