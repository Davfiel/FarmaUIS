from django.contrib import admin
from .models import Producto, Categoria, Medicamento

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion') 
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cantidad', 'fecha_entrada')
    search_fields = ('nombre',)

fieldsets = (
    (None, { 
        'fields': ('nombre', 'codigo_barras', 'categoria', 'fabricante', 'presentacion')
    }),
    ('Detalles de Venta y Stock', {
        'fields': ('precio_venta', 'stock_minimo', 'requiere_receta', 'ubicacion_almacen', 'activo')
    }),
    ('Descripción', {
        'classes': ('collapse',), 
        'fields': ('descripcion',),
    }),
)

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'principio_activo', 'dosis', 'fecha_vencimiento', 'venta_libre')
    search_fields = ('nombre', 'principio_activo')
    list_filter = ('venta_libre', 'fecha_vencimiento')