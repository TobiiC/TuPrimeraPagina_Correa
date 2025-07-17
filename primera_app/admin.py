from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Vendedor, Producto, Cliente

admin.site.register(Vendedor)
admin.site.register(Producto)
admin.site.register(Cliente)

class UserAdmin(BaseUserAdmin): 
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    search_fields = ('username', 'first_name', 'last_name', 'email')
    
    readonly_fields = ('date_joined', 'last_login')
    
    fieldsets = (
        ('Usuario - Contraseña', {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    ) 

admin.site.unregister(User) 

admin.site.register(User, UserAdmin)