from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

class Turno(models.Model):
    nome = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

class Serie(models.Model):
    nome = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome

class UF(models.Model):
    nome = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome_completo = models.CharField(max_length=100, null=True)
    data_nascimento = models.DateField(null=True)
    cpf = models.CharField(max_length=14, null=True, unique=True)
    rg = models.CharField(max_length=20, null=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, null=True)
    email = models.EmailField(null=True, unique=True)
    telefone = models.CharField(max_length=20, null=True)
    telefone_emergencial = models.CharField(max_length=20, null=False)
    cep = models.CharField(max_length=10, null=True)
    endereco = models.CharField(max_length=100, null=True)
    numero = models.CharField(max_length=10, null=True)
    complemento = models.TextField()
    bairro = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE, null=True)
    matricula = models.IntegerField(null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True)
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE, null=True)
    observacao = models.TextField()

    def __str__(self):
        return f"{self.nome_completo} - {self.matricula}"



