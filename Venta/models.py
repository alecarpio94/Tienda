from django.db import models
from Inventario.models import Producto
# Create your models here.

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(max_length=11)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre+" - "+str(self.cedula)


class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    cliente = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return "Factura #" + str(self.id)