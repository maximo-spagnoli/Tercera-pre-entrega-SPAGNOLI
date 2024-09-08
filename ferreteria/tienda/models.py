from django.db import models
from django.core.exceptions import ValidationError

def validate_stock(value):
    if value < 0:
        raise ValidationError('El stock no puede ser negativo.')

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.IntegerField(validators=[validate_stock])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
