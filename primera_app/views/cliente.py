from django.shortcuts import render,redirect
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from primera_app.models import cliente
from primera_app.forms import cliente_formulario
from django.http import HttpResponse

def clientes(request):
    clientes = cliente.objects.all()
    context = {"mensaje": "¡Bienvenido a la sección de clientes!"}
    return render(request, "primera_app/clientes.html", {"clientes": clientes})

def formulario_cliente(request):
    if request.method == "POST":
        formularioCliente = cliente_formulario(request.POST)
        if formularioCliente.is_valid():
            formularioCliente.save()
            return redirect('clientes') 
    else:
        formularioCliente = cliente_formulario()
    
    return render(request, "primera_app/formularios/formulario_cliente.html", {"formularioCliente": formularioCliente})