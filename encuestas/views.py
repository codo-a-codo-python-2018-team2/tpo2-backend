from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gretting(request):
    return HttpResponse("Hello world from Django for Codo a Codo 4.0")

def jose(request):
    return HttpResponse("Esta es la respuesta creada por Jose Guevara")
