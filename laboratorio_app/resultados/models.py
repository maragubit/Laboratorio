from django.db import models

# Create your models here.
class Resultado(models.Model):
    INFORME_CHOICES = (
        (0,'No'),
        (1,'Sí'),
    )
    muestra=models.ForeignKey('muestras.Muestra',on_delete=models.CASCADE,related_name='muestra_resultado')
    parametro=models.ForeignKey('parametros.Parametro',on_delete=models.SET_NULL, null=True, related_name='parametro_resultado')
    n1=models.CharField(max_length=20, blank=True, null=True)
    n2=models.CharField(max_length=20, blank=True, null=True)
    n3=models.CharField(max_length=20, blank=True, null=True)
    n4=models.CharField(max_length=20, blank=True, null=True)
    n5=models.CharField(max_length=20, blank=True, null=True)
    informe=models.IntegerField(choices=INFORME_CHOICES,)

    def __str__(self):
        return ('{}, {}').format(self.muestra,self.parametro)