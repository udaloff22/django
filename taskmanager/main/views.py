from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def pes(request):
    return render(request, 'main/pes.html')

def dogg(request):
    return render(request, 'main/dog.html')

def sobaka(request):
    return render(request, 'main/sobaka.html')

def pidor(request):
    return render(request, 'main/pidor.html')
