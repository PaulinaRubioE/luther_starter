from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Producto
from django.db.models import Q

def home(request):
    q = request.GET.get('q', '')
    if q:
        productos = Producto.objects.filter(nombre__icontains=q).prefetch_related('imagenes')
    else:
        productos = Producto.objects.all().prefetch_related('imagenes')

    destacados = Producto.objects.filter(destacado=True).prefetch_related('imagenes')[:3]

    context = {
        'productos': productos,
        'destacados': destacados,
        'query': q,
    }
    return render(request, 'productos/home.html', context)

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle.html', {'producto': producto})

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')
        # Aquí puedes guardar el mensaje o enviarlo por email. Por ahora mostramos mensaje de éxito.
        messages.success(request, "Gracias por contactarnos. En breve nos comunicaremos contigo.")
        return redirect('contacto')
    return render(request, 'productos/contacto.html')

def nosotros(request):
    return render(request, 'productos/nosotros.html')

# Vista mínima para el carrito (placeholder)
def cart_detail(request):
    # En esta etapa devolvemos una plantilla vacía/placeholder
    cart_items = []  # más adelante integrarás la lógica del carrito
    total = 0
    return render(request, 'productos/cart_detail.html', {'cart_items': cart_items, 'total': total})
