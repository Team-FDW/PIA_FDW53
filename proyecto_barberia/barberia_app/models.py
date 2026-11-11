from django.db import models

# Create your models here.
# servicios, estilistas, productos, sucursales y clientes.
class Servicio(models.Model):
    clave =models.CharField(max_length=10)
    nombre =models.CharField(max_length=50)
    descricion = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

class Estilista(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    especialidad = models.CharField(max_length=50)
    horario_entrada = models.TimeField()
    horario_salida = models.TimeField()
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

class Producto(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

class Sucursale(models.Model):
    clave = models.CharField(max_length=10)
    calle = models.CharField(max_length = 80)
    municipio = models.CharField(max_length = 80)
    numero_ext = models.CharField(max_length = 10)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

class Cliente(models.Model):
    clave = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(max_length=254, unique=True, )
    puntos = models.IntegerField()
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

