from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from .models import Parametro
from clientes.models import Cliente
from clientes.forms import ClienteForm
from .forms import ParametroForm
# Create your views here.
def parametroslist(request):
    parametros= Parametro.objects.all()
    return render(request,'parametros/parametros_list.html',{'parametros':parametros})


class ParametroCreate(CreateView):
    template_name = "parametros/crearparametro.html"
    model = Parametro
    form_class= ParametroForm
    def get_success_url(self):
        return reverse_lazy('parametroslist')


class ParametroDetailView(DetailView):

    model = Parametro
    template_name='parametros/parametro.html'


def parametrodelete(request,*args,**kwargs):
    pk=kwargs['pk']
    parametro=Parametro.objects.get(pk=pk)
    parametro.delete()
    return HttpResponseRedirect(reverse('parametroslist'))


class ParametroUpdate(UpdateView):
    model = Parametro
    template_name = "parametros/editarparametro.html"
    form_class= ParametroForm
    def get_success_url(self):
        return reverse_lazy('parametro', args=[self.object.id])