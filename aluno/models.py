from django.db import models

class Aluno(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    TURNO_CHOICES = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]
    STATUS_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]
    UF_CHOICES = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    # Informações pessoais
    nome_completo = models.CharField(max_length=150)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=20, unique=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    # Contato
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    telefone_emergencia = models.CharField(max_length=15, blank=True, null=True)

    # Endereço
    cep = models.CharField(max_length=9)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True, null=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)

    # Acadêmico
    numero_matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    ano = models.IntegerField(max_length=4, help_text="Ano de ingresso")
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='A')

    def __str__(self):
        return f"{self.numero_matricula} - {self.nome_completo}"
