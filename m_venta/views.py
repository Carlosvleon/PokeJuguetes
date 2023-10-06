from django.shortcuts import render, redirect
from .models import Venta, Detalle_Venta
from m_carrito.models import Carrito
from django.contrib.auth.decorators import login_required
from m_carrito.context_processor import total_carrito
from m_productos.models import Producto
from django.urls import reverse
from m_carrito.views import limpiar_carrito




# Create your views here.
def v_historial(request):
    contexto = {
        'venta': Venta.objects.filter(id_usuario__username = request.user.username),
        'detalle_venta': Detalle_Venta.objects.all()
    }
    return render(request, 'historial.html', contexto)

def v_boleta(request, venta_id):
    venta = Venta.objects.filter(id=venta_id, id_usuario=request.user)
    detalle_venta = Detalle_Venta.objects.filter(id_venta=venta_id)
    contexto = {
        'venta': venta,
        'detalle_venta': detalle_venta
    }
    # print(venta_id)
    return render(request, 'boleta.html', contexto)


@login_required(login_url='/usuario/login')

def procesar_venta(request):
    monto_total = total_carrito(request)["total_carrito"]
    venta = Venta.objects.create(id_usuario=request.user, monto_total = monto_total)
    carrito = Carrito.objects.filter(id_usuario=request.user)
    lista_venta= []
    for item in carrito:
        producto = item.id_producto
        cantidad_comprada = item.cantidad
        producto.stock_producto -= cantidad_comprada
        producto.save()
        lista_venta.append(Detalle_Venta(
            id_producto=producto,
            cant_producto=cantidad_comprada,
            valor_producto=producto.valor_producto,
            id_venta=venta
        ))
    Detalle_Venta.objects.bulk_create(lista_venta)
    limpiar_carrito(request)
    # print('print_2 ',venta)
    return redirect(reverse('v_boleta', args=[venta.id]))