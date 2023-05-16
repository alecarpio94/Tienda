from django.db import models

# Create your models here.


class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Unidades(models.Model):
    Nombre = models.CharField(max_length=50)
    Cantidad = models.IntegerField()
    def __str__(self):
        return self.Nombre

class Productos(models.Model):
    categoria = models.ManyToManyField(
        Categorias,
        #default=None,
    )
    Nombre = models.CharField(max_length=25)
    Precio = models.IntegerField()
    Cantidad = models.IntegerField()
    Medida = models.ManyToManyField(
        Unidades,
        #default=None,
    )
    def __str__(self):
        #return self.Nombre, self.Medida
        return self.Nombre