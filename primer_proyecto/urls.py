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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

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
    path('avatar/', usuario.actualizar_avatar, name="editar_avatar"),
    path('cerrar_sesion/', LogoutView.as_view(template_name='primera_app/usuario/cerrar_sesion.html'), name="cerrar_sesion"),
    path('editar_producto/<int:id_producto>/', producto.editar_producto, name="editar_producto"),
    path('editar_cliente/<int:id_cliente>/', cliente.editar_cliente, name="editar_cliente"),
    path('editar_vendedor/<int:id_vendedor>/', vendedor.editar_vendedor, name="editar_vendedor"),
    path('eliminar_producto/<int:id_producto>/', producto.eliminar_producto, name="eliminar_producto"),
    path('eliminar_cliente/<int:id_cliente>/', cliente.eliminar_cliente, name="eliminar_cliente"),
    path('eliminar_vendedor/<int:id_vendedor>/', vendedor.eliminar_vendedor, name="eliminar_vendedor"),
    path('cambiar_contrasenia/', usuario.cambiar_contrasenia, name="cambiar_contrasenia"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)