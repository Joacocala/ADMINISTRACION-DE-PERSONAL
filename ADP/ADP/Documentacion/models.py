from django.db import models
from Colaboradores.models import Empleado







class Documentacion(models.Model):
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE,null=True)
    venc_examen_periodico = models.DateField()
    venc_lic_conducir = models.DateField()
    venc_man_defensivo = models.DateField()

    def __str__(self):
        return self.empleado.nombre

