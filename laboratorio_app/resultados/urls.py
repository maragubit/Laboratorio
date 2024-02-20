from django.urls import path
from resultados import views
from .views import *







urlpatterns = [

    path("", views.resultadoslist , name="resultadoslist"),
    path("resultado/muestra/<int:pk>",ResultadoDetailView.as_view() , name="resultado"),
    path("resultado/agregar/muestra/<int:pk>",views.crearresultado , name="crearresultado"),
    path("resultado/editar/muestra/<int:pk>",views.editarresultado , name="editarresultado"),
    path("resultado/borrar/muestra/<int:pk>",views.resultadodelete , name="borrarresultado"),







]