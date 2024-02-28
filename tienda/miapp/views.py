from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

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

class SinglesList(ListView):
    model = Singles

class  SinglesCreate(CreateView):
    model = Singles
    fields = ['nombre', 'precio', 'cantidad']
    success_url = reverse_lazy('singles')

class  SinglesUpdate(UpdateView):
    model = Singles
    fields = ['nombre', 'precio', 'cantidad']
    success_url = reverse_lazy('singles')

class  SinglesDelete(DeleteView):
    model = Singles
    success_url = reverse_lazy('singles')





