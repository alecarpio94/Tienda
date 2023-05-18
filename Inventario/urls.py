from django.urls import path

from . import views

app_name = "Inventario"
urlpatterns = [
    path("", views.ProductoView.as_view(), name="index"),
    path("detalle/<int:pk>", views.DetalleProductoView.as_view(), name="details"),
]
