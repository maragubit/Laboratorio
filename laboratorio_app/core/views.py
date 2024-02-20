from django.shortcuts import render
import datetime
from datetime import timedelta

# Create your views here.
def home(request):

    return render(request,"core/portada.html")


def calendar(request):
    meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre', 'Noviembre', 'Diciembre']
    from clientes.models import Cliente
    clientes=Cliente.objects.exclude(frecuencia=0).order_by('proxima_visita')
    hoy=datetime.datetime.today()
    mes=meses[hoy.month-1]
    return render(request,'core/calendar.html',{'clientes':clientes,'hoy':hoy,'mes':mes})