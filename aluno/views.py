from django.shortcuts import render, get_object_or_404, redirect
from .models import Aluno
from .forms import AlunoForms

def index(request):
    alunos_total = Aluno.objects.count()
    return render(request, 'aluno/index.html', {'alunos_total': alunos_total})

def alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/alunos.html', {'alunos': alunos})

def alunos_detail(request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/alunos_detail.html', {'alunos': alunos})

def alunos_create(request):
    form = AlunoForms(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('alunos')
    else:
        form = AlunoForms()
    return render(request, 'aluno/alunos_forms.html', {'form': form})

def alunos_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForms(request.POST or None, instance=aluno)
    if request.method == 'POST':
        if form.is_valid():
            form.save
            return redirect('alunos')
    else:
        form = AlunoForms(instance=aluno)
    return render(request, 'aluno/alunos_forms.html', {'form': form})

def alunos_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    aluno.delete()
    return redirect('alunos')





