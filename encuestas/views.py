from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "base.html")


def update(data):
    pass


def create(data):
    pass


def delete(data):
    pass


def read(data):
    return HttpResponse("READ Hello world from Django for Codo a Codo 4.0:")


def gretting(request):
    print(dict(request.GET))

    HttpResponse("Hello world from Django for Codo a Codo 4.0:")

    if request.method == "GET":
        my_response = read(request)
    elif request.method == "UPDATE":
        my_response = update(request)
    elif request.method == "QUE VA?":
        my_response = delete(request)
    else:  # Que method es?
        my_response = create(request)

    return my_response


def natalia(request):
    return HttpResponse("Respuesta creada por Natalia")


def sofia(request):
    return HttpResponse("Esta es la respuesta de Sofía Ferro")


def jose(request):
    return HttpResponse("Esta es la respuesta creada por Jose Guevara")


def reinid(request):
    return HttpResponse("Esta es la respuesta creada por Reinid Valarino")
