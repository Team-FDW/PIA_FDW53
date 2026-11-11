from django.contrib import admin
from .models import Cliente,Estilista,Producto,Servicio,Sucursale
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Estilista)
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Sucursale)