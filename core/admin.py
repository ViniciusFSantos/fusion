from django.contrib import admin
from .models import Cargo, Servicos, Colaborador

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'modificado')
    
@admin.register(Servicos)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'icon', 'ativo', 'modificado')

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'modificado')