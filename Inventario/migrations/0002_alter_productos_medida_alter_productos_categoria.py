# Generated by Django 4.2.1 on 2023-05-16 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='Medida',
            field=models.ManyToManyField(to='Inventario.unidades'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='categoria',
            field=models.ManyToManyField(to='Inventario.categorias'),
        ),
    ]