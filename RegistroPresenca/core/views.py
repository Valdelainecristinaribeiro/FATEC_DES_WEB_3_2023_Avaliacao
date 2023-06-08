from django.shortcuts import redirect, render
from .forms import RegistroModelForm
from .models import RegistroModel

def registrar(request):
    if request.method == 'POST':
        form = RegistroModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:registrar')
    else:
        form = RegistroModelForm()
    return render(request, 'registrar.html', {'form': form})

def listar(request):
    professores = RegistroModel.OPCOES_PROFESSOR
    professor_selecionado = request.GET.get('professor', '')

    if professor_selecionado:
        alunos = RegistroModel.objects.filter(professor=professor_selecionado)
        contexto = {
            'professores': professores,
            'professor_selecionado': professor_selecionado,
            'alunos': alunos
        }
    else:
        contexto = {
            'professores': professores,
            'professor_selecionado': '',
            'alunos': []
        }

    return render(request, 'listar.html', contexto)