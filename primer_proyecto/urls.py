"""
URL configuration for primer_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from primera_app.views import cliente, vendedor, producto, usuario, views

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('inicio/',views.index, name="index"),
    path('productos/', producto.productos, name="productos"),
    path('clientes/', cliente.clientes, name="clientes"),
    path('busqueda/', views.buscar, name="buscar"),
    path('vendedores/', vendedor.vendedores, name="vendedores"),
    path('formulario_vendedor/', vendedor.formulario_vendedor, name="formulario_vendedor"),
    path('formulario_cliente/', cliente.formulario_cliente, name="formulario_cliente"),
    path('formulario_producto/', producto.formulario_producto, name="formulario_producto"),
    path('resultados_busqueda/', views.resultados_busqueda, name="resultados_busqueda"),
    path('acerca_de_mi/', views.acerca_de_mi, name="acerca_de_mi"),
    path('inicio_sesion/', usuario.iniciar_sesion, name="inicio_sesion"),
    path('editar_perfil/', usuario.edicion_perfil, name="editar_perfil"),
    path('registrarse/', usuario.registrarse, name="registrarse"),
    
]
