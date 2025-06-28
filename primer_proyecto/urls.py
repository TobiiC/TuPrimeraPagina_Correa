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

from primera_app import views

urlpatterns = [    
    path('admin/', admin.site.urls),
    path('inicio/',views.index, name="index"),
    path('productos/', views.productos, name="productos"),
    path('clientes/', views.clientes, name="clientes"),
    path('busqueda/', views.buscar, name="buscar"),
    path('vendedores/', views.vendedores, name="vendedores"),
    path('formulario_vendedor/', views.formulario_vendedor, name="formulario_vendedor"),
    path('formulario_cliente/', views.formulario_cliente, name="formulario_cliente"),
    path('formulario_producto/', views.formulario_producto, name="formulario_producto"),
    path('resultados_busqueda/', views.resultados_busqueda, name="resultados_busqueda")
    ]
