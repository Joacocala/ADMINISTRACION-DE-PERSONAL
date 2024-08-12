from django.contrib import admin
from .models import Documentacion



# Register your models here.

from django.contrib import admin
from .models import Documentacion

@admin.register(Documentacion)
class DocumentacionAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'venc_examen_periodico', 'venc_lic_conducir', 'venc_man_defensivo')
