from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

class ProductoView(generic.ListView):
    template_name = "index.html"
    context_object_name = "productos"

    def get_queryset(self):
        return Producto.objects.order_by("-pk")[:5]

class DetalleProductoView(generic.DetailView):
    model = Producto
    template_name = "detalle.html"