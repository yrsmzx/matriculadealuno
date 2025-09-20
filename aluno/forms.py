from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from .models import Aluno

class AlunoForm(ModelForm):
        
    cpf = forms.CharField(
        label="CPF",
        validators=[RegexValidator(
            regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
            message="Digite o CPF no formato 000.000.000-00"
        )],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    rg = forms.CharField(
        label="RG",
        validators=[RegexValidator(
            regex=r'^\d{10}-\d$',
            message="Digite o RG no formato XXXXXXXXXX-X (10 dígitos + hífen + 1 dígito)"
        )],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefone = forms.CharField(
        label="Telefone",
        validators=[RegexValidator(
            regex=r'^\(\d{2}\) \d{4}-\d{4}$',
            message="Digite o telefone no formato (00) 0000-0000"
        )],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    telefone_emergencia = forms.CharField(
        label="Telefone Emergência",
        required=False,
        validators=[RegexValidator(
            regex=r'^\(\d{2}\) \d{4}-\d{4}$',
            message="Digite o telefone no formato (00) 0000-0000"
        )],
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'uf': forms.Select(attrs={'class': 'form-control'}),
            'numero_matricula': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'turno': forms.Select(attrs={'class': 'form-control'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),    
            
        }

