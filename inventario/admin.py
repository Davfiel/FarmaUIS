from django.contrib import admin
from .models import Producto, Lote, MovimientoInventario

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'precio', 'fecha_entrada')
    search_fields = ('nombre',)
    list_filter = ('fecha_entrada',)

@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'fecha_llegada')
    search_fields = ('producto__nombre',)
    list_filter = ('fecha_llegada',)

@admin.register(MovimientoInventario)
class MovimientoInventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'tipo', 'fecha', 'lote')
    search_fields = ('producto__nombre',)
    list_filter = ('tipo', 'fecha')

