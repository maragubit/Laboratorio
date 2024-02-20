from django.db import models

# Create your models here.

class Parametro(models.Model):
    PRESENCIA_CHOICES = (
        ('SI','sí'),
        ('NO','no')
    )
    DILUCION_CHOICES = (
        ('-1','10^-1'),
        ('-2','10^-2'),
        ('-3','10^-3'),
        ('-4','10^-4'),
        ('-5','10^-5'),
        ('N/D','sin determinar'),
    )
    nombre=models.CharField(max_length=100)
    nombre_informe=models.CharField(verbose_name='nombre en el informe de la muestra',max_length=100, blank=True,null=True)
    metodo_ensayo=models.CharField(max_length=100, blank=True,null=True)
    presencia=models.CharField(verbose_name='Determinar presencia o ausencia' ,choices=PRESENCIA_CHOICES, default='NO', max_length=50)
    dilucion=models.CharField(choices=DILUCION_CHOICES, default='N/D',max_length=50)

    class Meta():
        ordering = ['nombre']


    def __str__(self):
        return ('{}').format(self.nombre)