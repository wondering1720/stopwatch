from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Esta es la pagina de inicio de mi aplicacion.")

def about(request):
    return HttpResponse("Esta es la pagina 'Aecrca de'.")
