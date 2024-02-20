from django.shortcuts import render
from .forms import MuestraForm
from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from django_xhtml2pdf.utils import pdf_decorator


# Create your views here.
def nuevamuestra(request,*args,**kwargs):
    from muestreos.models import Muestreo
    form=MuestraForm()
    pk=kwargs['pk']
    muestreo=Muestreo.objects.get(pk=pk)
    if request.method== 'POST':
        form=MuestraForm(request.POST)
        if form.is_valid():
            objeto=form.save(commit=False)
            objeto.muestreo=muestreo
            objeto.save()
            form.save_m2m()
            form=MuestraForm()
            return HttpResponseRedirect(reverse('muestreo', args=[pk]))
    return render(request,'muestras/nuevamuestra.html',{'form':form})

class MuestrasListView(ListView):
    model= Muestra
    template_name = 'muestras/muestras.html'
class MuestraDetailView(DetailView):

    model = Muestra
    template_name='muestras/muestra.html'




class MuestraUpdate(UpdateView):
    model = Muestra
    template_name = "muestras/editarmuestra.html"
    form_class= MuestraForm
    def get_success_url(self):
        return reverse_lazy('muestra', args=[self.object.id])


def muestradelete(request,*args,**kwargs):
    pk=kwargs['pk']
    muestra=Muestra.objects.get(pk=pk)
    muestreo_id=muestra.muestreo.id
    muestra.delete()
    return HttpResponseRedirect(reverse('muestreo',args=[muestreo_id]))





@pdf_decorator(pdfname='informe.pdf')
def informe(request,**kwargs):
    id=kwargs['pk']
    muestra=Muestra.objects.get(id=id)
    muestras = Muestra.objects.filter(muestreo=muestra.muestreo,superficie='SI')
    return render(request,'muestras/informe.html',{'muestra':muestra, 'muestras':muestras})