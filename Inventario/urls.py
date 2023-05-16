from django.urls import path
from . import views

app_name = 'Inventario'
urlpatterns = [
    path("/", views.IndexView.as_view(), name="index"),
    path("/producto/<int:pk>/", views.ProductosView.as_view(), name="productos"),
    path("/categoria/<int:pk/", views.CategoriasView.as_view(), name="categorias"),
    path("/unidad/<int:pk/", views.UnidadesView.as_view(), name="unidades"),
]
