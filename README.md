# TuPrimeraPagina-Correa

Iniciar el servidor
Ejecutá python manage.py runserver y abrilo en tu navegador.

Ver estructura general (herencia de plantillas)
Visitá cualquier página del sitio (por ejemplo, /inicio/, /productos/, etc.) para ver el diseño común extendido desde la plantilla base (padre.html).

Todas las plantillas HTML heredan de padre.html, incluyendo:

Páginas principales: index.html, clientes.html, productos.html, vendedores.html

Formularios: formulario_cliente.html, formulario_producto.html, formulario_vendedor.html, busqueda.html, resultados_busqueda.html

Cargar datos con formularios (uno por cada modelo):

Cada sección tiene un botón para cargar datos. Si no redirecciona correctamente, se puede acceder directamente por URL:

🛒 Agregar producto: /formulario_producto/

👤 Agregar cliente: /formulario_cliente/

🧑‍💼 Agregar vendedor: /formulario_vendedor/

Visualizar los datos cargados:

Podés ver los datos desde el panel de Django Admin o desde las URLs correspondientes:

Acceso al admin: /admin/
(crear superusuario con python manage.py createsuperuser)

O bien desde las páginas:

Ver productos: /productos/

Ver clientes: /clientes/

Ver vendedores: /vendedores/


Probar búsqueda en base de datos:

En la pestaña /productos/ hay un botón para buscar productos. También podés acceder directamente:

Formulario de búsqueda: /busqueda/

Ubicación de archivos importantes:
Plantillas principales:
primera_app/templates/primera_app/

Formularios HTML:
primera_app/templates/primera_app/formularios/

Lógica de negocio y estructura:

views.py: definiciones de vistas

forms.py: formularios de carga

models.py: clases de modelo (Producto, Cliente, Vendedor)

admin.py: registro de modelos para el admin

Rutas del proyecto:
primer_proyecto/urls.py



 Autor
Tobías Correa
🔗 GitHub: TobiiC