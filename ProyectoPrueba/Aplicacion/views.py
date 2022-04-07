from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def inicio(request):
    return render(request, "Aplicacion/inicio.html")

def crearAviso(request):
    return render(request, "Aplicacion/crearAviso.html")

def perfilMusico(request):
    return render(request, "Aplicacion/perfilMusico.html")