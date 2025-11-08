from django.core.management.base import BaseCommand
from productos.models import Sucursal, Producto, Inventario

class Command(BaseCommand):
    help = 'Seed database with sample sucursales, productos and inventarios'

    def handle(self, *args, **options):
        # clear existing
        Sucursal.objects.all().delete()
        Producto.objects.all().delete()

        s1 = Sucursal.objects.create(nombre='Luther Centro', ciudad='Guadalajara', direccion='Calle Principal 123')
        s2 = Sucursal.objects.create(nombre='Luther Norte', ciudad='Zapopan', direccion='Av. Norte 456')

        p1 = Producto.objects.create(codigo='LTH-001', nombre='Zapato Deportivo X', descripcion='Zapato cómodo para uso diario', categoria='Deportivos', marca='Luther', precio=799.00)
        p2 = Producto.objects.create(codigo='LTH-002', nombre='Sandalia Playa Y', descripcion='Sandalia ligera y resistente', categoria='Sandalias', marca='Luther', precio=399.00)
        p3 = Producto.objects.create(codigo='LTH-003', nombre='Bota Trabajo Z', descripcion='Bota reforzada para trabajo rudo', categoria='Botas', marca='Luther', precio=1299.00)

        Inventario.objects.create(producto=p1, sucursal=s1, cantidad=12)
        Inventario.objects.create(producto=p1, sucursal=s2, cantidad=5)
        Inventario.objects.create(producto=p2, sucursal=s1, cantidad=20)
        Inventario.objects.create(producto=p2, sucursal=s2, cantidad=8)
        Inventario.objects.create(producto=p3, sucursal=s1, cantidad=4)
        Inventario.objects.create(producto=p3, sucursal=s2, cantidad=0)

        self.stdout.write(self.style.SUCCESS('Sample data created successfully.'))
