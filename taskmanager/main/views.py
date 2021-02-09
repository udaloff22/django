from django.shortcuts import render
from .services import note, main_page

# Create your views here.

def index(request):
    return render(request, 'main/index.html', main_page(request))

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

def create(request):
    return note(request)
