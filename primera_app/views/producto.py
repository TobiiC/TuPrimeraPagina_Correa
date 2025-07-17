from django.shortcuts import render,redirect
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from primera_app.models import Producto
from primera_app.forms import producto_formulario
from django.http import HttpResponse

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'primera_app/productos/productos.html', {'productos': productos})

def formulario_producto(request):
    if request.method == "POST":
        formularioProducto = producto_formulario(request.POST)
        if formularioProducto.is_valid():
            formularioProducto.save()
            return redirect('productos') 
    else:
        formularioProducto = producto_formulario()
    
    return render(request, "primera_app/formularios/formulario_producto.html", {"formularioProducto": formularioProducto})

def eliminar_producto(request, id_producto):
 
    producto = Producto.objects.get(id=id_producto) 
    producto.delete()
 
    return productos(request)

def editar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        formularioProducto = producto_formulario(request.POST)
        if formularioProducto.is_valid():
            informacion = formularioProducto.cleaned_data
            producto.nombre = informacion['nombre']
            producto.descripcion = informacion['descripcion']
            producto.precio = informacion['precio']
            producto.save()
            return productos(request)

    else:
        formularioProducto = producto_formulario(
            initial={
                'nombre': producto.nombre,
                'descripcion': producto.descripcion,
                'precio': producto.precio,
                }
        )
           

    return render(request, "primera_app/productos/editar_producto.html", {"formularioProducto": formularioProducto, "id_producto": producto.id})