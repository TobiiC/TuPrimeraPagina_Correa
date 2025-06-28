from django import forms
from .models import vendedor, producto, cliente

class vendedor_formulario(forms.ModelForm):
    class Meta:
        model = vendedor
        fields = ['nombre', 'apellido', 'email']
        widgets = {
            'email': forms.EmailInput(),
        }


class producto_formulario(forms.ModelForm):
    class Meta:
        model = producto
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'codigo_producto': forms.NumberInput(),
        }

class cliente_formulario(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ['nombre', 'email']
        widgets = {
            'email': forms.EmailInput(),
        }