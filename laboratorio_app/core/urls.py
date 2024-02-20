from django.urls import path
from core import views







urlpatterns = [

    path("", views.home , name="portada"),
    path("calendar", views.calendar , name="calendar"),

]