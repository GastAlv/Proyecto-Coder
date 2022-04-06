from django.urls import path
from Aplicacion import views

urlpatterns = [
    path('crearaviso', views.crearAviso),
]