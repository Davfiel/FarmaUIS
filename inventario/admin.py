from django.contrib import admin
from .models import Producto, Lote, MovimientoInventario

admin.site.register(Producto)
admin.site.register(Lote)
admin.site.register(MovimientoInventario)
