from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all() # Obtiene todos los productos de la BD
    context = {'productos': productos}
    return render(request, 'productos/lista_productos.html', context)

