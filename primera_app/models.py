from django.db import models

class vendedor(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"Vendedor: {self.username}, Email: {self.email}"

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