from django.shortcuts import render,redirect
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from primera_app.models import Cliente
from primera_app.forms import cliente_formulario
from django.http import HttpResponse

def clientes(request):
    clientes = Cliente.objects.all()
    context = {"mensaje": "¡Bienvenido a la sección de clientes!"}
    return render(request, "primera_app/clientes/clientes.html", {"clientes": clientes})

def formulario_cliente(request):
    if request.method == "POST":
        formularioCliente = cliente_formulario(request.POST)
        if formularioCliente.is_valid():
            formularioCliente.save()
            return redirect('clientes') 
    else:
        formularioCliente = cliente_formulario()
    
    return render(request, "primera_app/formularios/formulario_cliente.html", {"formularioCliente": formularioCliente})

def eliminar_cliente(request, id_Cliente):
 
    cliente = Cliente.objects.get(id=id_Cliente) 
    cliente.delete()
 
    return clientes(request)

def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    if request.method == 'POST':
        formularioCliente = cliente_formulario(request.POST)
        if formularioCliente.is_valid():
            informacion = formularioCliente.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.email = informacion['email']
            cliente.save()
            return clientes(request)

    else:
        formularioCliente = cliente_formulario(
            initial={
                'nombre': cliente.nombre,
                'email': cliente.email,
                }
        )
           

    return render(request, "primera_app/clientes/editar_cliente.html", {"formularioCliente": formularioCliente, "id_cliente": cliente.id})
