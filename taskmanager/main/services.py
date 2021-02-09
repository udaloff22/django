from .models import TaskForm, Task
from django.shortcuts import redirect, render



def note(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.save()
        return redirect('main')

    form = TaskForm

    context = {'form' : form}

    return render(request, 'main/create.html', context )


def main_page(request): # вывод заметок на главной странице

    tasks = Task.objects.order_by('id')

    list = {
        'title' : 'Tha Main Page!',
        'tasks' : tasks,
        }

    return list
