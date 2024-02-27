from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    return render (request,"miapp/home.html")
def singles(request):
    return render (request,"miapp/singles.html")
def productosellado(request):
    return render (request,"miapp/productosellado.html")
def cliente(request):
    return render (request,"miapp/cliente.html")
def ofertas(request):
    return render (request,"miapp/ofertas.html")






