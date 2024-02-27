
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cliente/', cliente, name="cliente"),
    path('ofertas/', ofertas, name="ofertas"),
    path('singles/', singles, name="singles"),
    path('productosellado/', productosellado, name="productosellado"),
    
]