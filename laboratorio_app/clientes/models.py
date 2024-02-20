from django.db import models
from datetime import datetime
from datetime import timedelta
from muestreos.models import Muestreo
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

# Create your models here.
class Cliente(models.Model):
    FRECUENCIA_CHOICES = (
        (0,'sin determinar'),
        (15,'15 días'),
        (30,'1 mes'),
        (60,'2 meses'),
        (90,'3 meses'),
        (120,'4 meses'),
        (150,'5 meses'),
        (180,'6 meses'),

    )
    nombre=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100, blank=True, null=True)
    direccion=models.CharField(max_length=100, blank=True, null=True)
    email=models.EmailField(max_length=100, blank=True, null=True)
    frecuencia=models.IntegerField(choices=FRECUENCIA_CHOICES, default=0,)
    proxima_visita=models.DateField(null=True,blank=True)
    actividad=models.CharField(max_length=200, blank=True, null=True)


    class Meta():
        ordering = ['nombre']

    def save(self, *args, **kwargs):
        if self.muestra_cliente.all():
            muestreos=self.muestra_cliente.all()
            muestreo=muestreos.first()
            self.proxima_visita=muestreo.fecha + timedelta(days=self.frecuencia)
            super().save(*args, **kwargs)
        else:
            self.proxima_visita=None
            super().save(*args, **kwargs)


    def __str__(self):
        return ('{}').format(self.nombre)


@receiver(post_save, sender=Muestreo)
@receiver(post_delete, sender=Muestreo)
def actualizar_proxima_visita(sender, **kwargs):
    for cliente in Cliente.objects.all():
        cliente.save()