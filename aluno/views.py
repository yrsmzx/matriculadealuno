from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForm

def index(request):
    alunos_total = Aluno.objects.count()
    return render(request, 'aluno/home.html', {'alunos_total': alunos_total})

def alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/alunos.html', {'alunos': alunos})

def alunos_detail(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    return render(request, 'aluno/detalhes.html', {'aluno': aluno})

def alunos_create(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos')
    else:
        form = AlunoForm()
    return render(request, 'aluno/aluno_forms.html', {'form': form})

def alunos_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'aluno/aluno_forms.html', {'form': form})

def alunos_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    if request.method == 'POST':
        aluno.delete()
        return redirect('alunos')
    return render(request,{'aluno': aluno})






