from django.shortcuts import render
from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

# Create your views here.
def login(request):
    if request.method == "POST":

        email = request.POST["email"]
        senha = request.POST["password"]
        
        usuario = authenticate(request, email=email, password=senha)

        if usuario is not None:
            django_login(request, usuario)
            return render(request, "logado.html")

        return HttpResponseRedirect("/")

@login_required       
def logout(request):
    django_logout(request)
    return HttpResponseRedirect("/")