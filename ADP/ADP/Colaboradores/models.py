from django.db import models

#Determinar las opciones de los campos zona,estado,torre y convenio.
CONVENIO_OPCIONES = {
    "PP": "Petroleros Privados",
    "PJ": "Petroleros Jerarquicos"
}

ZONA_OPCIONES = {
    "CS": "CAÑADON SECO",
    "LH": "LAS HERAS",
    "CH": "CHUBUT",
    "TDF": "TIERRA DEL FUEGO",
    "REGIONAL": "REGIONAL"
}

ESTADO_OPCIONES = {
    "ACT": "ACTIVO",
    "IN": "INACTIVO"
}

TORRE_OPCIONES = {
    "COM": "COMUNICACIONES",
    "INFRA": "INFRAESTRUCTURA",
    "SOP": "SERVICIOS DIGITALES",
    "OD": "ON DEMAND",
    "GDA": "GESTION DE ACTIVOS"
}




#Se crea la clase que tendra los campos necesario de cada empleado, esta debera tener una relacion con DOCUMENTACION y AUSENTISMOS
class Empleado(models.Model):
    legajo = models.IntegerField(null=False)
    estado = models.CharField(
        max_length=15,  
        choices=[(k, v) for k, v in ESTADO_OPCIONES.items()],
    )
    zona = models.CharField(
        max_length=220,  
        choices=[(k, v) for k, v in ZONA_OPCIONES.items()],null=True    
    )


    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.IntegerField(null=False,default=0)
    email = models.EmailField()
    num_telefono = models.IntegerField()
    fecha_ingreso = models.DateField(null=True)
    fecha_nacimiento = models.DateField(null=False)
    torre_servicio = models.CharField(
        max_length=220,  
        choices=[(k, v) for k, v in TORRE_OPCIONES.items()],
    )

    puesto = models.CharField(max_length=100)
    convenio = models.CharField(
        max_length=2,  
        choices=[(k, v) for k, v in CONVENIO_OPCIONES.items()],
    )


    def __str__(self):
        return self.nombre +"    "+ self.apellido  +"  |  "+ self.torre_servicio +"  |  "+ self.puesto +"  |  "+ self.zona +"  |  "+ self.convenio