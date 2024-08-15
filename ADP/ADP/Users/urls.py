from Users import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login",views.login_request,name="Login"),
    path("register",views.register,name="Register"),
    path("logout", LogoutView.as_view(template_name= "inicio.html"),name='Logout'),
    path("about",views.About,name="about"),
    path("editarperfil",views.editarPerfil,name="EditarPerfil"),
    path("cambiarpassword",views.CambiarPassword.as_view(),name="CambiarPassword")
]