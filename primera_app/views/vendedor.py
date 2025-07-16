from django.shortcuts import render,redirect
from django.views.generic import ListView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from primera_app.models import vendedor
from primera_app.forms import vendedor_formulario
from django.http import HttpResponse

def vendedores(request):
    vendedores = vendedor.objects.all()
    context = {"mensaje": "¡Bienvenido a la sección de vendedores!"}
    return render(request, "primera_app/vendedores.html", {"vendedores": vendedores})

def formulario_vendedor(request):
    if request.method == "POST":
        formularioVendedor = vendedor_formulario(request.POST)
        if formularioVendedor.is_valid():
            formularioVendedor.save()
            return redirect('vendedores')
    else:
        formularioVendedor = vendedor_formulario()
    
    return render(request, "primera_app/formularios/formulario_vendedor.html", {"formularioVendedor": formularioVendedor})
