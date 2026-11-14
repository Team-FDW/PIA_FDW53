from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('equipo/', views.equipo, name="equipo"),
    path('servicios/', views.servicios, name="servicios"),
    path('productos/', views.productos, name="productos"),
    path('clientes/', views.clientes, name="clientes"),
    path('sucursales/', views.sucursales, name="sucursales"),
]
