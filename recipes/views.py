from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')


def sobre(request):
    return HttpResponse('Area Sobre - 02')


def contato(request):
    return HttpResponse('Area Contato - 03')

