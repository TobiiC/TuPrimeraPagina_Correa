from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from primera_app.forms import registrarse_formulario, editar_perfil, avatar_formulario
from ..models import avatar

def iniciar_sesion(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

        return redirect('inicio')

    form = AuthenticationForm()

    return render(request, "primera_app/usuario/inicio_sesion.html", {"form": form})

def registrarse(request):

      if request.method == 'POST':

            form = registrarse_formulario(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"primera_app/templates/primera_app/index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:      
            form = registrarse_formulario()     

      return render(request,"primera_app/usuario/registrarse.html" ,  {"form":form})


@login_required 
def edicion_perfil(request):
    usuario = request.user
    
    if usuario.is_staff == True:
         print("El usuario está activo")

    if request.method == 'POST':

        miFormulario = editar_perfil(request.POST, instance=usuario)

        if miFormulario.is_valid():

            miFormulario.save()

            return redirect('inicio')

    else:

        miFormulario = editar_perfil(instance=usuario)

    return render(request, "primera_app/usuario/editar.html", {"form": miFormulario, "usuario": usuario})


@login_required
def actualizar_avatar(request):
    avatar = avatar.objects.filter(user=request.user.id).first()
    if request.method == 'POST':
        form = avatar_formulario(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = avatar_formulario(instance=avatar)
    return render(request, '', {'form': form})