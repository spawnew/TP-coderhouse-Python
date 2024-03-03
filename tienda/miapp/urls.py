from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('ofertas/', ofertas, name="ofertas"),
   
    path('producto/', ProductoList.as_view(), name="producto"),
    path('create_producto/', ProductoCreate.as_view(), name="create_producto" ),    
    path('update_producto/<int:pk>/', ProductoUpdate.as_view(), name="update_producto" ),
    path('delete_producto/<int:pk>/', ProductoDelete.as_view(), name="delete_producto" ),
    path('buscar/', buscar, name="buscar"),
    path('buscarProductos/', buscarProductos, name="buscarProductos"),
 
    
    
    path('singles/', SinglesList.as_view() , name="singles" ),
    path('create_singles/', SinglesCreate.as_view(), name="create_singles" ),    
    path('update_singles/<int:pk>/', SinglesUpdate.as_view(), name="update_singles" ),
    path('delete_singles/<int:pk>/', SinglesDelete.as_view(), name="delete_singles" ),  




 path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
     path('logout/', LogoutView.as_view(template_name="miapp/logout.html"), name="logout"),
      path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar")

]
