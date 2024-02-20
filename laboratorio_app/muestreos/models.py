from django.db import models
from datetime import datetime

# Create your models here.
class Muestreo(models.Model):
    referencia=models.IntegerField( unique=True)
    cliente=models.ForeignKey('clientes.Cliente',related_name='muestra_cliente',on_delete=models.CASCADE)
    fecha=models.DateField(default=datetime.now)

    class Meta():
        ordering=['-referencia']
    def __str__(self):
        posicion=self.referencia
        ano=self.fecha.year
        return ('{}/{}').format(ano,posicion)