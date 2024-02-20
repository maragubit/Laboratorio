from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ResultadoForm
# Create your views here.
def resultadoslist(request):
    from muestreos.models import Muestreo
    muestreos= Muestreo.objects.all()
    return render(request,'resultados/resultados_list.html',{'muestreos':muestreos})

class ResultadoDetailView(DetailView):
    from muestras.models import Muestra
    model = Muestra
    template_name='resultados/resultado.html'



def crearresultado(request,*args,**kwargs):
    from muestras.models import Muestra
    from resultados.models import Resultado
    pk=kwargs['pk']
    muestra=Muestra.objects.get(pk=pk)
    if request.method =='POST':
        for parametro in muestra.parametros.all():
            if muestra.numero_muestras==5:
                parametropost1=str(parametro)+'n1'
                parametropost2=str(parametro)+'n2'
                parametropost3=str(parametro)+'n3'
                parametropost4=str(parametro)+'n4'
                parametropost5=str(parametro)+'n5'
                informe=request.POST.get('informe'+str(parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                parametron3=request.POST.get(parametropost3)
                parametron4=request.POST.get(parametropost4)
                parametron5=request.POST.get(parametropost5)
                resultado,created = Resultado.objects.get_or_create(muestra=muestra, parametro=parametro,
                                                            defaults={'n1':parametron1,'n2':parametron2,'n3':parametron3,'n4':parametron4,'n5':parametron5,'informe':informe})
                resultado.save()

            if muestra.numero_muestras==4:
                parametropost1=str(parametro)+'n1'
                parametropost2=str(parametro)+'n2'
                parametropost3=str(parametro)+'n3'
                parametropost4=str(parametro)+'n4'
                informe=request.POST.get('informe'+str(parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                parametron3=request.POST.get(parametropost3)
                parametron4=request.POST.get(parametropost4)
                resultado,created = Resultado.objects.get_or_create(muestra=muestra, parametro=parametro,
                                                                    defaults={'n1':parametron1,'n2':parametron2,'n3':parametron3,'n4':parametron4,'informe':informe})
                resultado.save()

            if muestra.numero_muestras==3:
                parametropost1=str(parametro)+'n1'
                parametropost2=str(parametro)+'n2'
                parametropost3=str(parametro)+'n3'
                informe=request.POST.get('informe'+str(parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                parametron3=request.POST.get(parametropost3)
                resultado,created = Resultado.objects.get_or_create(muestra=muestra, parametro=parametro,
                                                                    defaults={'n1':parametron1,'n2':parametron2,'n3':parametron3,'informe':informe})
                resultado.save()

            if muestra.numero_muestras==2:
                parametropost1=str(parametro)+'n1'
                parametropost2=str(parametro)+'n2'
                informe=request.POST.get('informe'+str(parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                resultado,created = Resultado.objects.get_or_create(muestra=muestra, parametro=parametro,
                                                                    defaults={'n1':parametron1,'n2':parametron2,'informe':informe})
                resultado.save()

            if muestra.numero_muestras==1:
                parametropost1=str(parametro)+'n1'
                informe=request.POST.get('informe'+str(parametro))
                parametron1=request.POST.get(parametropost1)
                resultado,created = Resultado.objects.get_or_create(muestra=muestra, parametro=parametro,
                                                                    defaults={'n1':parametron1,'informe':informe})
                resultado.save()

        return HttpResponseRedirect(reverse('resultado',args=[pk]))
    return render (request,"resultados/crearresultado.html",{'muestra':muestra})


def editarresultado(request,*args,**kwargs):
    from muestras.models import Muestra
    from resultados.models import Resultado
    pk=kwargs['pk']
    muestra=Muestra.objects.get(pk=pk)

    if request.method =='POST':

        for resultado in muestra.muestra_resultado.all():
            if muestra.numero_muestras==5:
                parametropost1=str(resultado.parametro)+'n1'
                parametropost2=str(resultado.parametro)+'n2'
                parametropost3=str(resultado.parametro)+'n3'
                parametropost4=str(resultado.parametro)+'n4'
                parametropost5=str(resultado.parametro)+'n5'
                informe=request.POST.get('informe'+str(resultado.parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                parametron3=request.POST.get(parametropost3)
                parametron4=request.POST.get(parametropost4)
                parametron5=request.POST.get(parametropost5)
                resultado= Resultado.objects.get(muestra=muestra, parametro=resultado.parametro)
                resultado.n1=parametron1
                resultado.n2=parametron2
                resultado.n3=parametron3
                resultado.n4=parametron4
                resultado.n5=parametron5
                resultado.informe=informe
                resultado.save()

            if muestra.numero_muestras==4:
                parametropost1=str(resultado.parametro)+'n1'
                parametropost2=str(resultado.parametro)+'n2'
                parametropost3=str(resultado.parametro)+'n3'
                parametropost4=str(resultado.parametro)+'n4'
                informe=request.POST.get('informe'+str(resultado.parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                parametron3=request.POST.get(parametropost3)
                parametron4=request.POST.get(parametropost4)
                resultado= Resultado.objects.get(muestra=muestra, parametro=resultado.parametro)
                resultado.n1=parametron1
                resultado.n2=parametron2
                resultado.n3=parametron3
                resultado.n4=parametron4
                resultado.informe=informe
                resultado.save()

            if muestra.numero_muestras==3:
                parametropost1=str(resultado.parametro)+'n1'
                parametropost2=str(resultado.parametro)+'n2'
                parametropost3=str(resultado.parametro)+'n3'
                informe=request.POST.get('informe'+str(resultado.parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                parametron3=request.POST.get(parametropost3)
                resultado= Resultado.objects.get(muestra=muestra, parametro=resultado.parametro)
                resultado.n1=parametron1
                resultado.n2=parametron2
                resultado.n3=parametron3
                resultado.informe=informe
                resultado.save()


            if muestra.numero_muestras==2:
                parametropost1=str(resultado.parametro)+'n1'
                parametropost2=str(resultado.parametro)+'n2'
                informe=request.POST.get('informe'+str(resultado.parametro))
                parametron1=request.POST.get(parametropost1)
                parametron2=request.POST.get(parametropost2)
                resultado= Resultado.objects.get(muestra=muestra, parametro=resultado.parametro)
                resultado.n1=parametron1
                resultado.n2=parametron2
                resultado.informe=informe
                resultado.save()


            if muestra.numero_muestras==1:
                parametropost1=str(resultado.parametro)+'n1'
                informe=request.POST.get('informe'+str(resultado.parametro))
                parametron1=request.POST.get(parametropost1)
                resultado= Resultado.objects.get(muestra=muestra, parametro=resultado.parametro)
                resultado.n1=parametron1
                resultado.informe=informe
                resultado.save()

        return HttpResponseRedirect(reverse('resultado',args=[pk]))
    return render (request,"resultados/editarresultado.html",{'muestra':muestra})


def resultadodelete(request,*args,**kwargs):
    from muestras.models import Muestra
    from resultados.models import Resultado
    pk=kwargs['pk']
    muestra=Muestra.objects.get(pk=pk)
    resultado=Resultado.objects.filter(muestra=muestra).delete()
    return HttpResponseRedirect(reverse('resultado',args=[pk]))