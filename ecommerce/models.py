from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen_url = models.URLField(max_length=1000, blank=True)

    def __str__(self):
        return self.nombre
