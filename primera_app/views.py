from django.shortcuts import render,redirect
from .models import producto, vendedor, cliente
from .forms import vendedor_formulario, cliente_formulario, producto_formulario
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {"mensaje": "¡Hola, mundo desde Django!"}
    return render(request, "primera_app/index.html", context)

def productos(request):
    productos = producto.objects.all()
    return render(request, 'primera_app/productos.html', {'productos': productos})


def clientes(request):
    clientes = cliente.objects.all()
    context = {"mensaje": "¡Bienvenido a la sección de clientes!"}
    return render(request, "primera_app/clientes.html", {"clientes": clientes})

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

def formulario_cliente(request):
    if request.method == "POST":
        formularioCliente = cliente_formulario(request.POST)
        if formularioCliente.is_valid():
            formularioCliente.save()
            return redirect('clientes')  # Redirige a la lista de clientes después de guardar
    else:
        formularioCliente = cliente_formulario()
    
    return render(request, "primera_app/formularios/formulario_cliente.html", {"formularioCliente": formularioCliente})

def formulario_producto(request):
    if request.method == "POST":
        formularioProducto = producto_formulario(request.POST)
        if formularioProducto.is_valid():
            formularioProducto.save()
            return redirect('productos')  # Redirige a la lista de productos después de guardar
    else:
        formularioProducto = producto_formulario()
    
    return render(request, "primera_app/formularios/formulario_producto.html", {"formularioProducto": formularioProducto})

def buscar(request):
    return render(request, "primera_app/formularios/busqueda.html")

def resultados_busqueda(request):
    if request.GET["nombre"]:
        nombre = request.GET['nombre']
        productos = producto.objects.filter(nombre__icontains=nombre)

        return render(request, "primera_app/formularios/resultados_busqueda.html", {"nombre": nombre, "productos": productos})

    else:
        respuesta = "No enviaste datos"

        return HttpResponse(respuesta)
    
def acerca_de_mi(request):
    return render(request, "primera_app/acerca.html")