from django.db import models
from datetime import datetime
from muestreos.models import Muestreo
from ckeditor.fields import RichTextField
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import post_delete

# Create your models here.

class Muestra(models.Model):
    N_CHOICES = (
        (1,'N1'),
        (2,'N2'),
        (3,'N3'),
        (4,'N4'),
        (5,'N5'),

    )
    SUPERFICIE_CHOICES = (
        ('SI','si'),
        ('NO','no'),
    )
    muestreo=models.ForeignKey('muestreos.Muestreo',on_delete=models.CASCADE,related_name='muestra_muestreo')
    nombre=models.CharField(max_length=100)
    informacion=models.TextField(blank=True, null=True)
    parametros=models.ManyToManyField('parametros.Parametro', blank=True)
    observaciones=models.TextField(blank=True,null=True)
    numero_muestras=models.IntegerField(choices=N_CHOICES, default=1,)
    numero_referencia_informe=models.CharField(max_length=50,blank=True,null=True)
    superficie=models.CharField(verbose_name='¿Es una superficie?',max_length=30,choices=SUPERFICIE_CHOICES, default='NO',)
    observaciones_informe=RichTextField(verbose_name='observaciones en informe' ,blank=True, null=True)
    transporte=models.CharField(max_length=200,blank=True,null=True)
    idinicial=models.IntegerField()
    idfinal=models.IntegerField()



    class Meta():
            ordering=['-id']

    def save(self,*args,**kwargs):
        muestreo=self.muestreo
        muestras=list(muestreo.muestra_muestreo.all())
        if len(muestras)== 1 and self in muestras:
            print('entramos en 1')
            inicial=1
            final=inicial+self.numero_muestras-1
            self.idinicial=inicial
            self.idfinal=final
            super().save(*args, **kwargs)


        elif len(muestras)>0:
            if self in muestras:

                posicion=muestras.index(self)
                if posicion != len(muestras)-1:
                    print('entramos en 2 a')
                    muestraanterior=muestras[posicion+1]
                    inicial=muestraanterior.idfinal +1
                    final=inicial+self.numero_muestras-1
                    self.idinicial=inicial
                    self.idfinal=final
                    super().save(*args, **kwargs)
                else:
                    print('entramos en 2 b')
                    inicial=1
                    final=inicial+self.numero_muestras-1
                    self.idinicial=inicial
                    self.idfinal=final
                    super().save(*args, **kwargs)

            else:
                muestraanterior=muestras[0]
                inicial=muestraanterior.idfinal +1
                final=inicial+self.numero_muestras-1
                self.idinicial=inicial
                self.idfinal=final
                super().save(*args, **kwargs)

        else:
            inicial=1
            final=inicial+self.numero_muestras-1
            self.idinicial=inicial
            self.idfinal=final
            super().save(*args, **kwargs)


    def __str__(self):
        if self.superficie=='SI':
            return ('{}/{} SUPERFICIE {}, {}').format(self.muestreo,self.idinicial,self.nombre, self.muestreo.cliente)
        else:

            if self.numero_muestras > 1:
                return ('{}/{}-{} {} {}').format(self.muestreo,self.idinicial,self.idfinal,self.nombre, self.muestreo.cliente)
            else:
                return ('{}/{} {} {}').format(self.muestreo,self.idinicial,self.nombre, self.muestreo.cliente)



@receiver(post_delete, sender=Muestra)
def actualizar_id(sender, **kwargs):
    for muestra in Muestra.objects.all().order_by('id'):
        muestra.save()