from django.urls import path
from parametros import views
from .views import *







urlpatterns = [

    path("", views.parametroslist , name="parametroslist"),
    path("parametro/<int:pk>", ParametroDetailView.as_view() , name="parametro"),
    path("editar/parametro/<int:pk>", ParametroUpdate.as_view() , name="editarparametro"),
    path("crear/parametro/", ParametroCreate.as_view() , name="crearparametro"),
    path("borrar/<int:pk>", views.parametrodelete, name="borrarparametro"),





]