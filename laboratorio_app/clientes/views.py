from django.shortcuts import render
from .models import *
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ClienteForm
# Create your views here.
def clienteslist(request):
    clientes= Cliente.objects.all()
    return render(request,'clientes/clientes_list.html',{'clientes':clientes})


class ClienteCreate(CreateView):
    template_name = "clientes/crearcliente.html"
    model = Cliente
    form_class= ClienteForm
    def get_success_url(self):
        return reverse_lazy('clienteslist')


class ClienteDetailView(DetailView):

    model = Cliente
    template_name='clientes/cliente.html'


def clientedelete(request,*args,**kwargs):
    pk=kwargs['pk']
    cliente=Cliente.objects.get(pk=pk)
    cliente.delete()
    return HttpResponseRedirect(reverse('clienteslist'))


class ClienteUpdate(UpdateView):
    model = Cliente
    template_name = "clientes/editarcliente.html"
    form_class= ClienteForm
    def get_success_url(self):
        return reverse_lazy('cliente', args=[self.object.id])