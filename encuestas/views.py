from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def gretting(request):
    return HttpResponse("Hello world from Django for Codo a Codo 4.0")

def natalia(request):
    return HttpResponse("Respuesta creada por Natalia")

def sofia(request):
    return HttpResponse("Esta es la respuesta de Sofía Ferro")

def jose(request):
    return HttpResponse("Esta es la respuesta creada por Jose Guevara")
