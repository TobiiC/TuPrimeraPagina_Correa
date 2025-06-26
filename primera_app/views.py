from django.shortcuts import render
from .models import producto

# Create your views here.

def index(request):
    context = {"mensaje": "¡Hola, mundo desde Django!"}
    return render(request, "primera_app/index.html", context)

def productos(request):
    productos = producto.objects.all()
    return render(request, 'primera_app/productos.html', {'productos': productos})


def clientes(request):
    context = {"mensaje": "¡Bienvenido a la sección de clientes!"}
    return render(request, "primera_app/clientes.html", context)

def vendedores(request):
    context = {"mensaje": "¡Bienvenido a la sección de vendedores!"}
    return render(request, "primera_app/vendedores.html", context)

def buscar(request):
    if request.method == "GET":
        query = request.GET.get("q", "")
        context = {"mensaje": f"Resultados de búsqueda para: {query}"}
    else:
        context = {"mensaje": "No se ha realizado ninguna búsqueda."}
    
    return render(request, "primera_app/busqueda.html", context)