from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from .forms import MuestreoForm
# Create your views here.
def muestreoslist(request):
    muestreos= Muestreo.objects.all()
    return render(request,'muestreos/muestreos_list.html',{'muestreos':muestreos})


class MuestreoDetailView(DetailView):

    model = Muestreo
    template_name='muestreos/muestreo.html'


def muestreosfecha(request,*args,**kwargs):
    pk=kwargs['pk']
    muestreo= Muestreo.objects.get(pk=pk)
    fecha=muestreo.fecha
    muestreos=Muestreo.objects.filter(fecha=fecha).order_by('referencia')
    return render(request,'muestreos/muestreos_fecha.html',{'muestreos':muestreos,'fecha':fecha})


class MuestreoUpdate(UpdateView):
    model = Muestreo
    template_name = "muestreos/muestreo_edit.html"
    form_class= MuestreoForm
    def get_success_url(self):
        return reverse_lazy('muestreo', args=[self.object.id])



class MuestreoCreate(CreateView):
    template_name = "muestreos/crearmuestreo.html"
    model = Muestreo
    form_class= MuestreoForm
    def get_success_url(self):
        return reverse_lazy('muestreo', args=[self.object.id])




def muestreodelete(request,*args,**kwargs):
    pk=kwargs['pk']
    muestreo=Muestreo.objects.get(pk=pk)
    muestreo.delete()
    return HttpResponseRedirect(reverse('muestreos'))