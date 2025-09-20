# Projeto Matrícula

Sistema de Matrícula em Django

## Sobre o Projeto

Este é um projeto desenvolvido para a disciplina de **Programação para Internet**, utilizando **Django 5.2.2**, uma framework de desenvolvimento web baseada em Python. O principal objetivo é criar um sistema de matrícula que permite a realização de operações CRUD (Create, Read, Update, Delete) para Aluno.

## Recursos Utilizados

* Django 5.2.2
* Python 3.x
* SQLite
* HTML/CSS/Bootstrap

## Funcionalidades

* CRUD de Alunos

## Instalação

### Pré-requisitos

Certifique-se de ter o **Python** e o **Django** instalados em seu computador com Windows.
Se ainda não tiver, instale pelo site oficial:

* [Python](https://www.python.org/downloads/)
* [Django](https://docs.djangoproject.com/en/4.2/topics/install/)

### Passos para instalação

1. **Clone o repositório**

```bash
git clone https://github.com/yrsmzx/matriculadealuno.git
```

2. **Entre na pasta do projeto**

```bash
cd matriculadealuno
```

3. **Crie um ambiente virtual**

```bash
python -m venv venv
```

4. **Ative o ambiente virtual**

```bash
venv\Scripts\activate
```

5. **Instale as dependências do projeto**

```bash
pip install -r requirements.txt
```

6. **Execute as migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Inicie o servidor**

```bash
python manage.py runserver
```

Agora, o sistema estará disponível em `http://localhost:8000`.