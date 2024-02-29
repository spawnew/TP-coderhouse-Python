from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *

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
    fields = ['nombre', 'precio', 'cantidad',]
    success_url = reverse_lazy('singles')

class  SinglesUpdate(UpdateView):
    model = Singles
    fields = ['nombre', 'precio', 'cantidad',]
    success_url = reverse_lazy('singles')

class  SinglesDelete(DeleteView):
    model = Singles
    success_url = reverse_lazy('singles')





def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            return render(request, "miapp/home.html")
        else:
            return redirect(reverse_lazy('login'))
        
    miForm = AuthenticationForm()

    return render(request, "miapp/login.html", {"form": miForm })    

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "miapp/registro.html", {"form": miForm })  