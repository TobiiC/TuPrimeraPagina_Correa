from django import forms
from .models import vendedor, producto, cliente

class VendedorForm(forms.ModelForm):
    class Meta:
        model = vendedor
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class producto(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'Codigo de Producto': forms.NumberInput(),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'email']
        widgets = {
            'email': forms.EmailInput(),
        }