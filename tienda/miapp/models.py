from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Singles (models.Model):
    
        nombre = models.CharField(max_length=40)
        precio = models.IntegerField()
        cantidad=models.IntegerField()
      
    

        def __str__(self):
             return f"{self.nombre}"
         
class Productosellado (models.Model):
        
        nombre = models.CharField(max_length=40)
        precio = models.IntegerField()
       

        def __str__(self):
             return f"{self.nombre}"
class Cliente (models.Model):
            
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    
    
class Ofertas(models.Model):
        
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()  
    descuento= models.IntegerField()      
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 