from django.contrib import admin
from .models import Producto, ImagenProducto, Sucursal, Inventario

class ImagenInline(admin.TabularInline):
    model = ImagenProducto
    extra = 1

class InventarioInline(admin.TabularInline):
    model = Inventario
    extra = 1

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'marca', 'categoria', 'precio', 'destacado')
    search_fields = ('codigo', 'nombre', 'marca', 'categoria')
    list_filter = ('categoria', 'marca', 'destacado')
    inlines = [ImagenInline, InventarioInline]

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'sucursal', 'cantidad')
