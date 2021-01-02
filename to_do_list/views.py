from django.shortcuts import render
from .forms import ItemsForms


def index(request):
    if request.method == 'POST':
        form = ItemsForms(request.post)
        if form.is_valid():
            form.save()
            print('Salvo com sucesso!')
        else:
            form = ItemsForms()  # tratamento de erro
    else:
        form = ItemsForms()

    return render(request, 'add-tarefa.html', {'form': form})