from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from primera_app.forms import registrarse_formulario, editar_perfil, avatar_formulario, cambiar_contrasenia_formulario
from ..models import Avatar
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def iniciar_sesion(request):

    if request.method == 'POST':
        formularioInicio = AuthenticationForm(request, data = request.POST)

        if formularioInicio.is_valid():

            usuario = formularioInicio.cleaned_data.get('username')
            contrasenia = formularioInicio.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Usuario o contraseña incorrectos. Por favor, volvé a intentarlo.")
        else:
            messages.error(request, "Usuario o contraseña inválidos. Verificá los datos e intentá de nuevo.")
    else:
        formularioInicio = AuthenticationForm()

    formularioInicio = AuthenticationForm()

    return render(request, "primera_app/usuario/inicio_sesion.html", {"form": formularioInicio})

def registrarse(request):

      if request.method == 'POST':

            formularioRegistro = registrarse_formulario(request.POST)
            if formularioRegistro.is_valid():
                user = formularioRegistro.save(commit=False)
                user.email = formularioRegistro.cleaned_data['email']
                user.first_name = formularioRegistro.cleaned_data['first_name']
                user.last_name = formularioRegistro.cleaned_data['last_name']
                user.save()
                  
                formularioRegistro.save()
                return render(request,"primera_app/usuario/registrarse.html" ,  {"mensaje":"Usuario Creado :)"})

      else:      
            formularioRegistro = registrarse_formulario()     

      return render(request,"primera_app/usuario/registrarse.html" ,  {"form":formularioRegistro})


@login_required 
def edicion_perfil(request):
    usuario = request.user
    
    if usuario.is_staff == True:
         print("El usuario está activo")

    if request.method == 'POST':

        formularioEditar = editar_perfil(request.POST, instance=usuario)

        if formularioEditar.is_valid():

            formularioEditar.save()

            return redirect('editar_perfil')

    else:

        formularioEditar = editar_perfil(instance=usuario)

    return render(request, "primera_app/usuario/editar.html", {"form": formularioEditar, "usuario": usuario})


@login_required
def actualizar_avatar(request):
    avatar_existente = Avatar.objects.filter(user=request.user).first()
    
    if request.method == 'POST':
        formularioAvatar = avatar_formulario(request.POST, request.FILES, instance=avatar_existente)
        if formularioAvatar.is_valid():
            avatar = formularioAvatar.save(commit=False)
            avatar.user = request.user 
            avatar.save()
            return redirect('index')
    else:
        formularioAvatar = avatar_formulario(instance=avatar_existente)

    return render(request, 'primera_app/usuario/cambiar_avatar.html', {'form': formularioAvatar})

@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('cerrar_sesion')

@login_required
def cambiar_contrasenia(request):
    if request.method == 'POST':
        formularioContra = cambiar_contrasenia_formulario(data=request.POST, request=request)
        if formularioContra.is_valid():
            user = request.user

            if user.check_password(formularioContra.cleaned_data.get('old_password')):
                user.set_password(formularioContra.cleaned_data.get('new_password1'))
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Contraseña cambiada exitosamente.")
                return redirect('index')
            else:
                messages.error(request, "La contraseña actual no es correcta.")
        else:
            messages.error(request, "Revisá los datos ingresados.")
    else:
        formularioContra = cambiar_contrasenia_formulario(request=request)

    return render(request, 'primera_app/usuario/cambiar_contrasenia.html', {'form': formularioContra})