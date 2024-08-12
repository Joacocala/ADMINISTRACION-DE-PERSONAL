from django.db import models

# Create your models here.


ESTADO_OPCIONES = {
    "Habilitada": "Habilitada",
    "Inhabilitada": "Inhabilitada"
}



class Bases(models.Model):
    zona = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=220,  
        choices=[(k, v) for k, v in ESTADO_OPCIONES.items()],
    )
    alarma = models.IntegerField()
    wifi = models.CharField(max_length=100)

