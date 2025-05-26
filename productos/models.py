from django.db import models
from django.db.models import Sum

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    cantidad = models.PositiveIntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_entrada = models.DateField(auto_now_add=True)
    
    def actualizar_cantidad(self):
        entradas = self.movimientoinventario_set.filter(tipo='entrada').aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        salidas = self.movimientoinventario_set.filter(tipo='salida').aggregate(Sum('cantidad'))['cantidad__sum'] or 0
    def __str__(self):
        return self.nombre

    

class Medicamento(Producto):
    principio_activo = models.CharField(max_length=200)
    dosis = models.CharField(max_length=100)
    fecha_vencimiento = models.DateField()
    venta_libre = models.BooleanField(default=True)