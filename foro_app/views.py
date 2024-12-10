from django.shortcuts import render

# Create your views here.


def Plantilla(request):
    return render (request, 'plantilla.html')

def home(request):
    return render (request, 'Home.html')