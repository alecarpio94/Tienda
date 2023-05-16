from django.shortcuts import render
from django.core.paginator import Paginator
from Inventario.models import Productos

# Create your views here.
def index(request):

    producto = Productos.objects.all()
    
    Paginator = Paginator(producto, 5)
    page = request.GET.get('page')
    productos_page = Paginator.get_page(page)

    return render(request, 'index.html', {'productos': productos_page})

