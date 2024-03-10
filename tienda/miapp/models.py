
from django.contrib.auth.models import User
from django.db import models
from django.db.models import ImageField


# Create your models here.
class Singles (models.Model):
        
        nombre = models.CharField(max_length=40)
        precio = models.IntegerField()
        cantidad=models.IntegerField()
        foto = ImageField (upload_to="media/avatares" , default="../media/avatares/images_4.jpeg")
        def __str__(self):
            return f"{self.user} {self.imagen}" 
        
        
        def __str__(self):
             return f"{self.nombre}"
         
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField()
    foto = ImageField(upload_to="media/avatares", default="../media/avatares/default_1.jpeg")

    

def __str__(self):
        return f"{self.user} {self.imagen}" 
class Cliente (models.Model):
            
    direccion=models.CharField(max_length=40)
    telefono=models.IntegerField()
    
    
class Oferta(models.Model):
        
    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()  
    descuento= models.IntegerField()      
    
class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 
    
    
    
class OrdenCompra(models.Model):
      nombre=models.CharField(max_length=40)
      precio=models.IntegerField()  
      mediopago = models.CharField(max_length=60 ,blank=True)