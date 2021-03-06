from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class Login(LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('core:index')
