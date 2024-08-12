from django.contrib import admin
from .models import Empleado



# Register your models here.
#admin.site.register(Empleado)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('legajo', 'nombre', 'apellido', 'email',"num_telefono")