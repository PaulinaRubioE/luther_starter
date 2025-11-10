from django.core.management.base import BaseCommand
from productos.models import Producto, Sucursal, Inventario, ImagenProducto
from django.core.files.base import ContentFile
import os

class Command(BaseCommand):
    help = "Seed DB with sample data"

    def handle(self, *args, **options):
        Producto.objects.all().delete()
        Sucursal.objects.all().delete()
        p1 = Producto.objects.create(codigo="LTH-001", nombre="Zapato Deportivo X", marca="Luther", categoria="Deportivos", descripcion="Cómodo para uso diario", precio=799)
        p2 = Producto.objects.create(codigo="LTH-002", nombre="Sandalia Playa Y", marca="Luther", categoria="Sandalias", descripcion="Ligera y resistente", precio=399)
        p3 = Producto.objects.create(codigo="LTH-003", nombre="Bota Trabajo Z", marca="Luther", categoria="Botas", descripcion="Reforzada para trabajo rudo", precio=1299)
        s1 = Sucursal.objects.create(nombre="Luther Centro", ciudad="Guadalajara")
        s2 = Sucursal.objects.create(nombre="Luther Norte", ciudad="Zapopan")
        Inventario.objects.create(producto=p1, sucursal=s1, cantidad=12)
        Inventario.objects.create(producto=p1, sucursal=s2, cantidad=5)
        Inventario.objects.create(producto=p2, sucursal=s1, cantidad=20)
        Inventario.objects.create(producto=p3, sucursal=s1, cantidad=4)
        self.stdout.write(self.style.SUCCESS("Sample data created"))
