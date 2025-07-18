# TuPrimeraPagina-Correa
# Web
La idea de la página es poder gestionar Clientes, Productos y Vendedores de un negocio. Con la posibilidad de agregar, eliminar y editar estos modelos solo para aquellos que esten logueados.

# Ejecucion

Iniciar el servidor
Ejecutá python manage.py runserver y abrilo en tu navegador.

Ver estructura general (herencia de plantillas)
Visitá cualquier página del sitio (por ejemplo, /inicio/, /productos/, etc.) para ver el diseño común extendido desde la plantilla base (padre.html).

Todas las plantillas HTML heredan de padre.html, incluyendo:

Páginas principales: index.html, clientes.html, productos.html, vendedores.html

Formularios: formulario_cliente.html, formulario_producto.html, formulario_vendedor.html, busqueda.html, resultados_busqueda.html

Cargar datos con formularios (uno por cada modelo):

Visualizar los datos cargados:

Podés ver los datos desde el panel de Django Admin o desde las URLs correspondientes:

Acceso al admin: /admin/
(crear superusuario con python manage.py createsuperuser)

O bien desde las páginas:
  
Ver productos: /productos/

Ver clientes: /clientes/

Ver vendedores: /vendedores/

Probar búsqueda en base de datos:

En la pestaña /productos/ va a estar la entrada de texto para buscar los productos.

Ubicación de archivos importantes:
Plantillas principales:
primera_app/templates/primera_app/

Formularios HTML:
primera_app/templates/primera_app/formularios/

Lógica de negocio y estructura:

primera_app/views: definiciones de vistas por modelo

forms.py: formularios de carga y edición

models.py: clases de modelo (Producto, Cliente, Vendedor, Avatar)

admin.py: registro de modelos para el admin

Rutas del proyecto:
primer_proyecto/urls.py

# Rutas de Usuarios logueados

Formularios de carga de modelos: formulario_cliente.html, formulario_producto.html, formulario_vendedor.html, busqueda.html, resultados_busqueda.html

Cargar datos con formularios (uno por cada modelo):

Cada sección tiene un botón para cargar datos. Si no, se puede acceder directamente por URL:

🛒 Agregar producto: /formulario_producto/

👤 Agregar cliente: /formulario_cliente/

🧑‍💼 Agregar vendedor: /formulario_vendedor/

👤 Gestión de usuario
🧾 Acerca de mí: /acerca_de_mi/

🔐 Iniciar sesión: /inicio_sesion/

🆕 Registrarse: /registrarse/

🖋 Editar perfil: /editar_perfil/

🖼 Cambiar avatar: /avatar/

🔒 Cambiar contraseña: /cambiar_contrasenia/

🚪 Cerrar sesión: /cerrar_sesion/

🛠 Gestión de datos (CRUD)
📝 Editar producto: /editar_producto/<id_producto>/

📝 Editar cliente: /editar_cliente/<id_cliente>/

📝 Editar vendedor: /editar_vendedor/<id_vendedor>/

❌ Eliminar producto: /eliminar_producto/<id_producto>/

❌ Eliminar cliente: /eliminar_cliente/<id_cliente>/

❌ Eliminar vendedor: /eliminar_vendedor/<id_vendedor>/

⚠️ Las rutas que contienen <id_*> requieren el identificador correspondiente del objeto a editar o eliminar.
Esto se puede seleccionar desde cada una de las tablas de las pestañas.

# Video Demostrativo
https://www.youtube.com/watch?v=GaLi5gQzC0U

 Autor
Tobías Correa
🔗 GitHub: TobiiC
