from django.db import models

class Sucursal(models.Model):
    nombre = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=120, blank=True)
    direccion = models.TextField(blank=True)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class ImagenProducto(models.Model):
    producto = models.ForeignKey(Producto, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='inventarios')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='inventarios')
    cantidad = models.PositiveIntegerField(default=0)
    class Meta:
        unique_together = ('producto','sucursal')
    def __str__(self):
        return f"{self.producto.codigo} - {self.sucursal.nombre}: {self.cantidad}"
