from django.urls import path
from . import views

app_name = 'Compras'
urlpatterns = [
    path("", views.index, name="index"),
]
