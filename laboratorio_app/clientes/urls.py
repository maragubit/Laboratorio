from django.urls import path
from clientes import views
from .views import *

urlpatterns = [

    path("", views.clienteslist , name="clienteslist"),
    path("crear", ClienteCreate.as_view(), name="clientecreate"),
    path("cliente/<int:pk>", ClienteDetailView.as_view(), name="cliente"),
    path("cliente/borrar/<int:pk>", views.clientedelete, name="clienteborrar"),
    path("cliente/editar/<int:pk>", ClienteUpdate.as_view(), name="editarcliente"),

]