from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Usuario
from django.contrib import messages

from accounts.forms import CreateUserForm, ChangeUserForm, UpdatePerfil


class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('core:index')


class Cadastro(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/cadastro.html'


class UpdateUsuario(UpdateView, LoginRequiredMixin):
    login_url = reverse_lazy('login')
    model = Usuario
    # fields = ('username', 'nome', 'telefone')
    template_name = 'accounts/update_usuario.html'
    form_class = UpdatePerfil
    success_message = 'Dados alterados com sucesso!'


    def get_success_url(self):
        return reverse('accounts:perfil',kwargs={"pk": self.request.user.id})

class ProfilePage(TemplateView):
    template_name = 'accounts/profile.html'
    def get_context_data(self, **kwargs):
        context = super(ProfilePage, self).get_context_data(**kwargs)
        # pass user id for which profile page was requested
        context['requested_profile_id'] = self.kwargs.get('pk')

        return context