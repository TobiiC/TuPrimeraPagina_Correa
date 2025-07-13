from django.db import models
from django.contrib.auth.models import User

class vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f"Vendedor: {self.nombre}, Email: {self.email}"

class producto(models.Model):
    codigo_producto = models.CharField(max_length=10, primary_key = True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"

class cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"