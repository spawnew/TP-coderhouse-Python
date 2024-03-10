from django.urls import path
from .views import *
from .views import restar



urlpatterns = [
    path('', home, name="home"),
  
   
   
    path('producto/', ProductoList.as_view(), name="producto"),
    path('create_producto/', ProductoCreate.as_view(), name="create_producto" ),    
    path('update_producto/<int:pk>/', ProductoUpdate.as_view(), name="update_producto" ),
    path('delete_producto/<int:pk>/', ProductoDelete.as_view(), name="delete_producto" ),
    path('buscar/', buscar, name="buscar"),
    path('buscarProductos/', buscarProductos, name="buscarProductos"),
 
      path('acerca',acerca, name='acerca'),
 
    
    path('cliente/', ClienteList.as_view() , name="cliente" ),
    path('create_cliente/',  ClienteCreate.as_view(), name="create_cliente" ),    
    path('update_cliente/<int:pk>/',  ClienteUpdate.as_view(), name="update_cliente" ),
    path('delete_cliente/<int:pk>/',  ClienteDelete.as_view(), name="delete_cliente" ),
    
    path('oferta/', OfertaList.as_view() , name="oferta" ),
    path('create_oferta/', OfertaCreate.as_view(), name="create_oferta" ),    
    path('update_oferta/<int:pk>/', OfertaUpdate.as_view(), name="update_oferta" ),
    path('delete_oferta/<int:pk>/', OfertaDelete.as_view(), name="delete_oferta" ),
    



 path('login/', login_request, name="login"),
  path('registro/', register, name="registro"),
  
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),
    
    
    path('singles/', SinglesList.as_view() , name="singles" ),
    path('create_singles/', SinglesCreate.as_view(), name="create_singles" ),    
    path('update_singles/<int:pk>/', SinglesUpdate.as_view(), name="update_singles" ),
    path('delete_singles/<int:pk>/', SinglesDelete.as_view(), name="delete_singles" ),  
    path ('salir/' , salir , name="salir"),
    path ('restar/' , restar , name="restar"),
  

]
