from django.contrib import admin
from imovel.models import Imovel, ImovelImagem, Endereco

# Register your models here.

admin.site.register(Endereco)


class ImovelImageAdmin(admin.StackedInline):
    model = ImovelImagem


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    inlines = [ImovelImageAdmin]

    class Meta:
        model = Imovel


@admin.register(ImovelImagem)
class ImovelImageAdmin(admin.ModelAdmin):
    pass
