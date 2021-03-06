from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import CreateUserForm


class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('core:index')


class Cadastro(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/cadastro.html'
