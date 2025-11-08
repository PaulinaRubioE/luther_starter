from django.shortcuts import render, get_object_or_404
from .models import Producto
from django.db.models import Q

def home(request):
    query = request.GET.get('q')
    if query:
        productos = Producto.objects.filter(nombre__icontains=query)
    else:
        productos = Producto.objects.all()

    # “Destacados”: por ahora tomamos los primeros 3 productos
    destacados = Producto.objects.all()[:3]

    return render(request, 'productos/home.html', {
        'productos': productos,
        'destacados': destacados,
        'query': query,
    })


def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto})
