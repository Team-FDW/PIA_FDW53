from django.shortcuts import render
from .models import Estilista

# Create your views here.
def index(request): 
    return render(request,"index.html")


def equipo(request):
    datos = {
        "estilistas": Estilista.objects.all()
    } 
    return render(request,"equipo.html", context=datos)



def servicios(request):
    return render(request, "servicios.html")

def productos(request):
    return render(request, "productos.html")

def clientes(request):
    return render(request, "clientes.html")

def sucursales(request):
    return render(request, "sucursales.html")

