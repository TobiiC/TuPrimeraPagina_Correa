from django import forms
from .models import Vendedor, Producto, Cliente, Avatar
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class vendedor_formulario(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido', 'email']
        widgets = {
            'email': forms.EmailInput(),
        }


class producto_formulario(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio']
        widgets = {
            'precio': forms.NumberInput(),
        }

class cliente_formulario(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email']
        widgets = {
            'email': forms.EmailInput(),
        }

class inicio_sesion_formulario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class registrarse_formulario(UserCreationForm):
    first_name = forms.CharField(max_length=20, label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=20, label='Apellido', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=20, label='Usuario', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Ingrese su Contraseña nuevamente', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
 
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'password1', 'password2')

class editar_perfil(UserChangeForm):
        password = None
        email = forms.EmailField(label="Ingrese su email:")
        username = forms.CharField(label="Nombre de usuario")
        last_name = forms.CharField()
        first_name = forms.CharField()
        is_active = forms.BooleanField(required=False, label="¿Está activo?")

        class Meta:
            model = User
            fields = ('username', 'email', 'last_name', 'first_name', 'is_active')

class cambiar_contrasenia_formulario(forms.Form):
    old_password = forms.CharField(label="Contraseña actual", widget=forms.PasswordInput)
    new_password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Repetir nueva contraseña", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Removemos request antes de llamar al super
        super().__init__(*args, **kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

class avatar_formulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']