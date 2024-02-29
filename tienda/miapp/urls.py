from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('ofertas/', ofertas, name="ofertas"),
   
    path('productosellado/', productosellado, name="productosellado"),
    
    
    path('singles/', SinglesList.as_view(), name="singles" ),
    path('create_singles/', SinglesCreate.as_view(), name="create_singles" ),    
    path('update_singles/<int:pk>/', SinglesUpdate.as_view(), name="update_singles" ),
    path('delete_singles/<int:pk>/', SinglesDelete.as_view(), name="delete_singles" ),  




 path('login/', login_request, name="login"),
    path('registro/', register, name="registro"),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),

]