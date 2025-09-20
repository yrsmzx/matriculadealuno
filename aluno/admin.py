from django.contrib import admin
from .models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('numero_matricula', 'nome_completo', 'curso', 'ano', 'turno', 'status', 'uf')
    list_filter = ('status', 'turno', 'uf', 'curso')
    search_fields = ('nome_completo', 'numero_matricula', 'cpf', 'rg')
    ordering = ('nome_completo',)
    fieldsets = (
        (None, {
            'fields': ('numero_matricula', 'nome_completo', 'data_nascimento', 'cpf', 'rg', 'sexo', 'email', 'telefone', 'telefone_emergencia')
        }),
        ('Endereço', {
            'fields': ('cep', 'endereco', 'numero', 'complemento', 'bairro', 'cidade', 'uf')
        }),
        ('Informações Acadêmicas', {
            'fields': ('curso', 'ano', 'turno', 'observacoes', 'status')
        }),
    )
    readonly_fields = ('numero_matricula',)
    