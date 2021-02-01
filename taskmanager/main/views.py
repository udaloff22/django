from django.shortcuts import render
from .models import Task

# Create your views here.

def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html',
        {
            'title' : 'Tha Main Page!',
            'tasks' : tasks,
        })

def about(request):
    return render(request, 'main/about.html')

def pes(request):
    return render(request, 'main/pes.html')

def dog(request):
    return render(request, 'main/dog.html')

def sobaka(request):
    return render(request, 'main/sobaka.html')

def pidor(request):
    return render(request, 'main/pidor.html')
