from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('ofertas/', ofertas, name="ofertas"),
   
    path('productosellado/', productosellado, name="productosellado"),
    
    
    path('singles/', SinglesList.as_view(), name="singles" ),
    path('create_singles/', SinglesCreate.as_view(), name="create_singles" ),    
    path('update_singles/', SinglesUpdate.as_view(), name="update_singles" ),
    path('delete_singles/', SinglesDelete.as_view(), name="delete_singles" ),  
]