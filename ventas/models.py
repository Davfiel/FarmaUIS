from django.db import models
from productos.models import Producto
from personas.models import Empleado

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    cliente = models.CharField(max_length=100)
    estado = models.CharField(
        max_length=20,
        choices=[('activa', 'Activa'), ('cancelada', 'Cancelada')],
        default='activa'
    )

    def calcular_total(self):
        return sum([detalle.calcular_subtotal() for detalle in self.detalleventa_set.all()])

    def __str__(self):
        return f"Venta {self.id} - {self.fecha.date()} - {self.cliente}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def calcular_subtotal(self):
        return self.cantidad * self.precio

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"

class Factura(models.Model):
    venta = models.OneToOneField(Venta, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    numero_factura = models.CharField(max_length=50)

    def __str__(self):
        return f"Factura {self.numero_factura} - Venta {self.venta.id}"
