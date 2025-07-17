from django.shortcuts import render,redirect
from ..models import Producto
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {"mensaje": "¡Hola, mundo desde Django!"}
    return render(request, "primera_app/index.html", context)

def buscar(request):
    return render(request, "primera_app/formularios/busqueda.html")

def resultados_busqueda(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        productos = Producto.objects.filter(nombre__icontains=nombre)

        return render(request, "primera_app/formularios/resultados_busqueda.html", {"nombre": nombre, "productos": productos})

    else:
        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)
    
def acerca_de_mi(request):
    return render(request, "primera_app/acerca.html")