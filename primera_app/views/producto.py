from django.shortcuts import render,redirect
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from primera_app.models import producto
from primera_app.forms import producto_formulario
from django.http import HttpResponse

def productos(request):
    productos = producto.objects.all()
    return render(request, 'primera_app/productos.html', {'productos': productos})

def formulario_producto(request):
    if request.method == "POST":
        formularioProducto = producto_formulario(request.POST)
        if formularioProducto.is_valid():
            formularioProducto.save()
            return redirect('productos') 
    else:
        formularioProducto = producto_formulario()
    
    return render(request, "primera_app/formularios/formulario_producto.html", {"formularioProducto": formularioProducto})