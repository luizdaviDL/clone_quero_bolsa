from django.contrib import admin
from .models import Curso,Universidade, Bairro,Cidade, Aviso, CadastroBolsa

admin.site.register(Curso)
admin.site.register(Universidade)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(Aviso)
@admin.register(CadastroBolsa)
class Cadastro_bolsa(admin.ModelAdmin):
    readonly_fields = ['nome', 'cpf', 'nascimento', 'email', 'cep', 'cidade', 'estado', 'universidade', 'curso']

