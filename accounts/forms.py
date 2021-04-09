from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.forms import ModelForm
from .models import Usuario


class CreateUserForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'nome', 'telefone', 'password1', 'password2']

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


class UpdatePerfil(ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'nome', 'telefone')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return email
        raise forms.ValidationError(f'Email {email} já exite')

    def save(self, commit=True):
        account = super(UpdatePerfil, self).save(commit=False)
        account.username = self.cleaned_data['username']
        # account.email = self.cleaned_data['email']
        account.nome = self.cleaned_data['nome']
        account.telefone = self.cleaned_data['telefone']
        if commit:
            account.save()
        return account
