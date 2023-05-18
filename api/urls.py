from django.urls import path
from rest_framework import routers

from Inventario.viewset import *

route = routers.SimpleRouter()
route.register('producto', ProductoViewSet)
route.register('categoria', CategoriaViewSet)
route.register('unidad', UnidadViewSet)
route.register('medida', MedidaViewSet)

urlpatterns = route.urls
