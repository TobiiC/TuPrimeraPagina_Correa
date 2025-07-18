from django.shortcuts import render,redirect
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from primera_app.models import Vendedor
from primera_app.forms import vendedor_formulario
from django.http import HttpResponse

def vendedores(request):
    vendedores = Vendedor.objects.all()
    context = {"mensaje": "¡Bienvenido a la sección de vendedores!"}
    return render(request, "primera_app/vendedores/vendedores.html", {"vendedores": vendedores})

def formulario_vendedor(request):
    if request.method == "POST":
        formularioVendedor = vendedor_formulario(request.POST)
        if formularioVendedor.is_valid():
            formularioVendedor.save()
            return redirect('vendedores')
    else:
        formularioVendedor = vendedor_formulario()
    
    return render(request, "primera_app/formularios/formulario_vendedor.html", {"formularioVendedor": formularioVendedor})

def eliminar_vendedor(request, id_vendedor):
 
    vendedor = Vendedor.objects.get(id=id_vendedor) 
    vendedor.delete()
 
    return vendedores(request)

def editar_vendedor(request, id_vendedor):
    vendedor = Vendedor.objects.get(id=id_vendedor)
    if request.method == 'POST':
        formularioVendedor = vendedor_formulario(request.POST)
        if formularioVendedor.is_valid():
            informacion = formularioVendedor.cleaned_data
            vendedor.nombre = informacion['nombre']
            vendedor.apellido = informacion['apellido']
            vendedor.email = informacion['email']
            vendedor.save()
            return vendedores(request)

    else:
        formularioVendedor = vendedor_formulario(
            initial={
                'nombre': vendedor.nombre,
                'apellido': vendedor.apellido,
                'email': vendedor.email,
                }
        )
           

    return render(request, "primera_app/vendedores/editar_vendedor.html", {"formularioVendedor": formularioVendedor, "id_vendedor": vendedor.id})
