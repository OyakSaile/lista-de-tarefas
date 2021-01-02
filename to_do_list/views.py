from django.shortcuts import render
from .forms import ItemsForms


def index(request):
    if request == 'POST':
        form = ItemsForms(request.post)
    else:
        form = ItemsForms()

    return render(request, 'add-tarefa.html', {'form': form})