
from .models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms      import AuthenticationForm
from django.contrib.auth            import authenticate, login,logout
from django.contrib.auth.mixins     import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages


# Create your views here.
def home(request):
    return render (request,"miapp/home.html")
def acerca(request):
    return render (request,"miapp/acerca.html")

def cliente(request):
    return render (request,"miapp/cliente.html")
def oferta(request):
    return render (request,"miapp/oferta.html")
def producto (request):
    contexto = {'producto': Producto.objects.all()}
    return render(request, "miapp/producto.html", contexto)




class SinglesList(LoginRequiredMixin, ListView):
    model = Singles

class  SinglesCreate(LoginRequiredMixin, CreateView):
    model = Singles
    fields = ['nombre', 'precio', 'cantidad','foto']
    success_url = reverse_lazy('singles')

class  SinglesUpdate(LoginRequiredMixin, UpdateView):
    model = Singles
    fields = ['nombre', 'precio', 'cantidad','foto']
    success_url = reverse_lazy('singles')

class  SinglesDelete(LoginRequiredMixin, DeleteView):
    model = Singles
    success_url = reverse_lazy('singles')




def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)

            #____ Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.jpg"
            finally:
                request.session["avatar"] = avatar
            #__________________________________________

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
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            user = User.objects.get(username=usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return render(request, "miapp/home.html")
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "miapp/editar_Perfil.html", {"form": form }) 

@login_required
def agregar_avatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request, "miapp/home.html")

    else:    
        form = AvatarForm()

    return render(request, "miapp/agregar_avatar.html", {"form": form })



 
@login_required
def buscar(request):
    return render(request, "miapp/buscar.html")

@login_required
def buscarProductos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        producto = Producto.objects.filter(nombre__icontains = patron)
        contexto = {"producto": producto }
        return render(request, "miapp/producto.html", contexto)
    return HttpResponse ("No se ingresaron patrones de busqueda")
    
class ProductoList(LoginRequiredMixin, ListView):
    model = Producto

class  ProductoCreate(LoginRequiredMixin, CreateView):
    model = Producto
    fields = ['nombre', 'precio','foto']
    success_url = reverse_lazy('producto')

class  ProductoUpdate(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = ['nombre', 'precio','foto']
    success_url = reverse_lazy('producto')

class  ProductoDelete(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('producto')
    
    
class OfertaList(LoginRequiredMixin, ListView):
    model = Oferta

class  OfertaCreate(LoginRequiredMixin, CreateView):
    model = Oferta
    fields = ['nombre' , 'precio' , 'descuento']
    success_url = reverse_lazy('oferta')

class  OfertaUpdate(LoginRequiredMixin, UpdateView):
    model =Oferta
    fields = ['nombre', 'precio','descuento']
    success_url = reverse_lazy('oferta')
class  OfertaDelete(LoginRequiredMixin, DeleteView):
        model = Oferta
        success_url = reverse_lazy('oferta')
        
        
class ClienteList(LoginRequiredMixin, ListView):
     model = Cliente

class  ClienteCreate(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['direccion', 'telefono']
    success_url = reverse_lazy('cliente')

class  ClienteUpdate(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['direccion', 'telefono']
    success_url = reverse_lazy('cliente')

class  ClienteDelete(LoginRequiredMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy('cliente')
    

def salir( request):
    logout(request)
    messages.success(request ,"tu sesision se ha cerrado correctamente")
    return redirect ("home")

def tu_vista(request):
    # Suponiendo que 'o' es un objeto de TuModelo que contiene los valores de la base de datos
    o = Oferta.objects.get(id=1)  # Ejemplo de cómo obtener un objeto de la base de datos

    # Realizar la resta de los valores de la base de datos
    resultado_resta = restar(o.precio, o.descuento)

    return render(request, 'oferta_list.html', {'o': o, 'resultado_resta': resultado_resta})

def restar(numero1, numero2):
    resta = numero1 - numero2
    return resta