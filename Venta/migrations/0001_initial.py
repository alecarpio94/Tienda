# Generated by Django 4.2.1 on 2023-05-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('Documento', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Telefono', models.IntegerField()),
                ('Direccion', models.CharField(max_length=250)),
                ('Ciudad', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Producto', models.ManyToManyField(default=None, to='Inventario.productos')),
                ('cliente', models.ManyToManyField(default=None, to='Venta.cliente')),
            ],
        ),
    ]
