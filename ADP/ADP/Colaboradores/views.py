from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from .models import Empleado
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login, logout, authenticate















# Create your views here.
def Index(request):
    return render(request,"inicio.html")

class EmpleadoList(ListView):
    model = Empleado
    context_object_name = "empleados"
    template_name = "lista_empleados.html"


class EmpleadoDetail(DetailView):
    model = Empleado
    template_name = "detalle_empleados.html"


class EmpleadoCrear(CreateView):
    model = Empleado
    template_name = "crear_empleado.html"
    success_url = reverse_lazy("lista_empleados")
    fields = "__all__"


class EmpleadoUpdate(UpdateView):
    model = Empleado
    template_name = "update_empleado.html"
    success_url = reverse_lazy("lista_empleados")
    fields = "__all__"


class EmpleadoBorrar(DeleteView):
    model = Empleado
    template_name = "borrar_empleado.html"
    success_url = reverse_lazy("lista_empleados")




