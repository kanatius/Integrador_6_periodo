from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Usuario


class CreateUserForm(UserCreationForm):

    class Meta:
        model: Usuario

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["username"]

        if commit:
            user.save()

        return user

class ChangeUserForm(UserChangeForm):

    class Meta:
        model: Usuario

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.nome = self.cleaned_data["nome"]
        user.sobrenome = self.cleaned_data["sobrenome"]
        user.telefone = self.cleaned_data["telefone"]

        if commit:
            user.save()

        return user
