from django.db import models
from Inventario.models import Productos
# Create your models here.

class Cliente(models.Model):
    Documento = models.IntegerField(primary_key=True)
    Nombre    = models.CharField(max_length=50)
    Email     = models.EmailField()
    Telefono  = models.IntegerField()
    Direccion = models.CharField(max_length=250)
    Ciudad    = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Documento)

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ManyToManyField(
        Cliente,
        default=None,
    )
    Producto = models.ManyToManyField(
        Productos,
        default=None,
    )

    def __str__(self):
        return str ("#" + str(self.id))