from django.db import models

# Create your models here.

class Compra(models.Model):
    fecha_compra = models.CharField(max_length=50)
    proveedor = models.CharField(max_length=50)
    importe_compra = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.proveedor}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.nombre}"
    
class Recurso(models.Model):
    nombre_recurso = models.CharField(max_length=50)
    unidad = models.CharField(max_length=50)
    agrupamiento = models.CharField(max_length=50)
    
    def __str__(self) :
        return f"{self.id} - {self.nombre_recurso}"






