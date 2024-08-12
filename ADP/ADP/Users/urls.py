from Users import views
from django.urls import path, include

urlpatterns = [
    path("login",views.login_request,name="Login"),
    path("register",views.register,name="Register"),
]