from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from Users.forms import UserRegisterForm
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from .models import *



def login_request(request):

    msg_login =""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje": f"Bienvenido {username}"})
        msg_login = "Credenciales incorrectas! intenta de nuevo"
    
    form = AuthenticationForm()
    return render(request, "login.html", {'form':form ,"msg_login":msg_login})


#se registra usuario mediante
def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request,"inicio.html", {"Mensaje": "Usuario Creado"})

    else:
        form = UserRegisterForm()
    
    return render(request, "registro.html", {"form":form })


def About(request):
    return render(request,"about.html")



#editar perfil de usuario
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)
        if miFormulario.is_valid():
            
            miFormulario.save()

           
            if 'imagen' in request.FILES:
               
                try:
                    avatar = Avatar.objects.get(user=usuario)
                except Avatar.DoesNotExist:
                    
                    avatar = Avatar(user=usuario)

               
                avatar.imagen = miFormulario.cleaned_data['imagen']
                avatar.save()

            return render(request, "inicio.html")
    else:
        miFormulario = UserEditForm(instance=usuario)
    
    return render(request, "editar_perfil.html", {"miFormulario": miFormulario, "usuario": usuario})





@method_decorator(csrf_protect, name='dispatch')
class CambiarPassword(LoginRequiredMixin,PasswordChangeView):
    template_name = "cambiar_password.html"
    success_url = reverse_lazy("EditarPerfil")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Tu contraseña ha sido cambiada exitosamente.")
        return response
    


