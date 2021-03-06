from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from .forms import *

# Register your models here.
UserAdmin.fieldsets += ('Custom', {'fields': ('nome', 'sobrenome', 'telefone')}),


class CustomUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = ChangeUserForm
    model = Usuario
    list_display = ['nome', 'sobrenome', 'telefone', 'email']
    readonly_fields = ['first_name', 'last_name']

admin.site.register(Usuario, CustomUserAdmin)