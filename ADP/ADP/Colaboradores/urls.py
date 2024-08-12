from django.urls import path
from Colaboradores import views

urlpatterns = [path("", views.Index, name="inicio"),
               path("empleados/lista",views.EmpleadoList.as_view(),name="lista_empleados"),
               path("crear",views.EmpleadoCrear.as_view(),name="crear_empleado"),
               path("empleados/<pk>",views.EmpleadoDetail.as_view(),name="detalle_empleados"),
               path("empleados/<pk>/editar",views.EmpleadoUpdate.as_view(), name="update_empleados"),
               path("empleados/<pk>/borrar",views.EmpleadoBorrar.as_view(),name="borrar_empleados"),
               


]