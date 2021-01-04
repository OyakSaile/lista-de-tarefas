from django.shortcuts import render
from .forms import ItemsForms


def index(request):
    if request.method == 'POST':
        form = ItemsForms(request.POST)
        if form.is_valid():
            form.save()
            print('Salvo com sucesso!')
        else:
            print('Formulário inválido!')
            print(form.errors)
            form = ItemsForms()  # tratamento de erro
    else:
        form = ItemsForms()
        print('Não veio POST')

    return render(request, 'add-tarefa.html', {'form': form})