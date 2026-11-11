from django.shortcuts import render
from .models import Estilista

# Create your views here.
def equipo(request):
    datos ={
        "estilistas": Estilista.objects.all()
    } 
    return render(request,"equipo.html",context=datos)