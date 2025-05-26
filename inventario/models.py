import datetime
from django.db import models
from django.db.models import Sum
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    fecha_entrada = models.DateField(auto_now_add=True)

    def actualizar_cantidad(self):
        entradas = self.movimientoinventario_set.filter(tipo='entrada').aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        salidas = self.movimientoinventario_set.filter(tipo='salida').aggregate(Sum('cantidad'))['cantidad__sum'] or 0
        self.cantidad = entradas - salidas
        self.save()

    def __str__(self):
        return self.nombre


class Lote(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField(default=0)
    fecha_llegada = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Lote de {self.producto.nombre if self.producto else 'Sin producto'} - {self.fecha_llegada}"


class MovimientoInventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('salida', 'Salida')])
    fecha = models.DateTimeField(auto_now_add=True)
    lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        # No permitir cantidades cero o negativas
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': 'La cantidad debe ser mayor que cero.'})

        # No permitir salidas mayores al stock disponible
        if self.tipo == 'salida' and self.cantidad > self.producto.cantidad:
            raise ValidationError({'cantidad': 'No hay suficiente stock para esta salida.'})

    def save(self, *args, **kwargs):
        self.full_clean()  # Ejecuta las validaciones antes de guardar
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tipo} - {self.producto.nombre} - {self.cantidad}"
