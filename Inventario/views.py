from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views import generic
from .models import *

# Create your views here.

class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "producto"
    def get_queryset(self):
        return Productos.objects.order_by("-id")[:5]
    
class ProductosView(generic.DetailView):
    model = Productos
    template_name = "productos.html"

    def get_queryset(self):
        return Productos.objects.all()
    
class CategoriasView(generic.DetailView):
    model = Categorias
    template_name = "categorias.html"
    
class UnidadesView(generic.DetailView):
    model = Unidades
    template_name = "unidades.html"
