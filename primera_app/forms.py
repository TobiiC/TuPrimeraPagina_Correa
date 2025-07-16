from django import forms
from .models import vendedor, producto, cliente, avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

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

class registrarse_formulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class editar_perfil(UserChangeForm):
        email = forms.EmailField(label="Ingrese su email:")
        password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
        username = forms.CharField(label="Nombre de usuario")

        last_name = forms.CharField()
        first_name = forms.CharField()
        is_active = forms.BooleanField(required=False, label="¿Está activo?")

        class Meta:
            model = User
            # fields = ('email', 'password')
            fields = ('username', 'email', 'last_name', 'first_name', 'is_active')

class avatar_formulario(forms.ModelForm):
    class Meta:
        model = avatar
        fields = ['imagen']