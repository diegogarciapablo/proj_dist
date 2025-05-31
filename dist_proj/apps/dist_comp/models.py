from django.db import models
from decimal import Decimal, ROUND_HALF_UP
from django.utils import timezone
import uuid

# === PRODUCTOS ===
class Producto(models.Model):
    codigo_barras = models.CharField(max_length=50, unique=True, verbose_name="Código de barras del proveedor")
    codigo_interno = models.CharField(max_length=12, unique=True, editable=True, verbose_name="Código interno")
    desc_producto = models.CharField(max_length=100, verbose_name="descripcion")
    clasificacion = models.CharField(max_length=100)
    unidad = models.CharField(max_length=12)
    marca = models.CharField(max_length=50)
    p_costo = models.DecimalField(max_digits=10, decimal_places=4, verbose_name="precio costo")
    p_venta = models.DecimalField(max_digits=10, decimal_places=1, verbose_name="precio venta")
    stock = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.codigo_interno:
            self.codigo_interno = str(uuid.uuid4().int)[:8]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.desc_producto} ({self.codigo_interno})"
    
    