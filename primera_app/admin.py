from django.contrib import admin
from .models import vendedor, producto, cliente

admin.site.register(vendedor)
admin.site.register(producto)
admin.site.register(cliente)
