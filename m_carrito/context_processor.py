from m_carrito.models import Carrito
from django.contrib.auth.decorators import login_required



def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        carrito_items = Carrito.objects.filter(id_usuario=request.user)
        for item in carrito_items:
            total += item.calcular_total()
    return {"total_carrito": total}

def total_unidades_carrito(request):
    total_unidades = 0
    if request.user.is_authenticated:
        carrito_items = Carrito.objects.filter(id_usuario=request.user)
        for item in carrito_items:
            total_unidades += item.cantidad
    return {"total_unidades_carrito": total_unidades}


def carrito_context(request):
    if request.user.is_authenticated:
        usuario = request.user
        carrito = Carrito.objects.filter(id_usuario=usuario)
        return {'carrito': carrito}
    return request

