from django.contrib import admin
from .models import Producto, ImagenProducto, Sucursal, Inventario

class ImagenInline(admin.TabularInline):
    model = ImagenProducto
    extra = 0

class InventarioInline(admin.TabularInline):
    model = Inventario
    extra = 0

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    inlines = [ImagenInline, InventarioInline]

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'sucursal', 'cantidad')


