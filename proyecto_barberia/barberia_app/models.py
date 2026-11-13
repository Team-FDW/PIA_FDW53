from django.db import models

# Create your models here.
# servicios, estilistas, productos, sucursales y clientes.
class Servicio(models.Model):
    clave = models.AutoField(primary_key = True)
    nombre =models.CharField(max_length=50)
    descripcion = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

class Estilista(models.Model):
    clave = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    especialidad = models.CharField(max_length=50)
    horario_entrada = models.TimeField()
    horario_salida = models.TimeField()
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    @property
    def mostrar_especialidad (self):
        return f"{self.especialidad}"
    @property
    def mostrar_horario(self):
        return f"{self.horario_entrada} a {self.horario_salida}"

    

class Producto(models.Model):
    clave = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=80)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre 

class Sucursale(models.Model):
    clave = models.AutoField(primary_key = True)
    calle = models.CharField(max_length = 80)
    municipio = models.CharField(max_length = 80)
    numero_ext = models.CharField(max_length = 10)
    telefono = models.CharField(max_length= 14)
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.calle 

class Cliente(models.Model):
    clave = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=80)
    apellido = models.CharField(max_length=80)
    email = models.EmailField(max_length=254, unique=True, )
    puntos = models.IntegerField()
    fecha_alta = models.DateField(auto_now_add=True)
    fecha_baja = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.nombre + "" + self.apellido

