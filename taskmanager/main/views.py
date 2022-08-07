from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def mytasks(request):
    error = ''
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Ошибка заполнения формы'

    tasks = Task.objects.order_by('id')
    return render(request, 'main/tasks.html', {'tasks': tasks, 'form': form, 'error': error})
