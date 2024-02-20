from django.urls import path
from muestras import views
from .views import *







urlpatterns = [

    path("crear/muestreo/<int:pk>", views.nuevamuestra , name="nuevamuestra"),
    path("muestras", MuestrasListView.as_view() , name="muestras"),
    path("muestra/<int:pk>", MuestraDetailView.as_view() , name="muestra"),
    path("editar/muestra/<int:pk>", MuestraUpdate.as_view() , name="editarmuestra"),
    path("borrar/<int:pk>", views.muestradelete, name="borrarmuestra"),
    path("muestra/informe/<int:pk>", views.informe , name="informe"),



]