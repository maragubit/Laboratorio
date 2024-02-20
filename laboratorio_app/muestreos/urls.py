from django.urls import path
from muestreos import views
from .views import *







urlpatterns = [

    path("", views.muestreoslist , name="muestreos"),
    path("muestreo/<int:pk>", MuestreoDetailView.as_view() , name="muestreo"),
    path("muestreos/fecha/<int:pk>", views.muestreosfecha , name="muestreosfecha"),
    path("editar/muestreo/<int:pk>", MuestreoUpdate.as_view() , name="editarmuestreo"),
    path("crear/muestreo", MuestreoCreate.as_view() , name="crearmuestreo"),
    path("borrar/<int:pk>", views.muestreodelete, name="borrarmuestreo"),





]