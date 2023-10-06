from django.shortcuts import render, redirect
from .models import Carrito
from m_productos.models import Producto
from sweetify import success, warning
# Create your views here.


def ver_carrito(request):
    # Obtén el usuario actual
    usuario = request.user
    if request.method == 'POST':
        # Obtén los datos enviados en el formulario POST
        producto_id = request.POST.get('producto_id')
        cantidad = int(request.POST.get('cantidad', 1))
        # Obtén el producto a partir del ID
        producto = Producto.objects.get(id=producto_id)
        # Comprueba si ya existe un ítem del carrito para este producto y usuario
        carrito_existente = Carrito.objects.filter(id_usuario=usuario, id_producto=producto).first()
        if carrito_existente:
            # Si ya existe, actualiza la cantidad
            carrito_existente.cantidad += cantidad
            carrito_existente.save()
        else:
            # Si no existe, crea un nuevo ítem del carrito
            carrito = Carrito(id_usuario=usuario, id_producto=producto, cantidad=cantidad)
            carrito.save()
        # Redirige a la página del carrito o a donde desees
        return redirect('carrito.html')
    else:  # Método GET
        # Obtén todos los ítems del carrito del usuario actual
        carrito_items = Carrito.objects.filter(id_usuario=request.user.id)
        context = {
            'carrito_items': carrito_items,
        }
        return render(request, 'carrito.html', context)
        
def agregar_al_carrito(request, producto_id):
    # Obtén el producto a partir del ID
    producto = Producto.objects.get(id=producto_id)
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtén el usuario actual
        usuario = request.user
        # Verifica si el producto ya está en el carrito del usuario
        carrito_existente = Carrito.objects.filter(id_usuario=usuario, id_producto=producto).first()
        if carrito_existente:
            if carrito_existente.cantidad + 1 > producto.stock_producto: #Aquí te valido el stock comparando con lo que ya hay dentro del carrito
                warning(request, f'No hay suficiente stock de {producto.nom_producto}. Solo hay {producto.stock_producto} en stock.')
            else:
                carrito_existente.cantidad += 1
                carrito_existente.save()
                success(request, 'El producto ha sido añadido al carrito.')
        else:
            if producto.stock_producto < 1: #Aquí te valido el stock comparando con stock -1 (porque el carro por defecto siempre añade de a 1)
                warning(request, f'No hay suficiente stock de {producto.nom_producto}. Solo hay {producto.stock_producto} en stock.')
            else:
                nuevo_carrito = Carrito(id_usuario=usuario, id_producto=producto, cantidad=1)
                nuevo_carrito.save()
                success(request, 'El producto ha sido añadido al carrito.')

        # Redirige a la página del carrito o a donde desees
        return redirect('v_productos')
    else:
        # Si el usuario no está autenticado, redirige a la página de inicio de sesión o muestra un mensaje de error
        return redirect('v_login')
    
def restar_producto(request, producto_id):
    # Obtén el producto a partir del ID
    producto = Producto.objects.get(id=producto_id)
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtén el usuario actual
        usuario = request.user
        # Verifica si el producto está en el carrito del usuario
        carrito_existente = Carrito.objects.filter(id_usuario=usuario, id_producto=producto).first()
        if carrito_existente:
            if carrito_existente.cantidad > 1:
                # Resta 1 a la cantidad del producto en el carrito
                carrito_existente.cantidad -= 1
                carrito_existente.save()
            else:
                # Si la cantidad es 1, elimina el producto del carrito
                carrito_existente.delete()

        # Redirige a la página del carrito o a donde desees
        return redirect('v_productos')
    else:
        # Si el usuario no está autenticado, redirige a la página de inicio de sesión o muestra un mensaje de error
        return redirect('v_login')

def limpiar_carrito(request):
    # Verifica si el usuario está autenticado
    if request.user.is_authenticated:
        # Obtén el usuario actual
        usuario = request.user
        # Elimina todos los productos del carrito para el usuario actual
        Carrito.objects.filter(id_usuario=usuario).delete()
        # Redirige a la página del carrito o a donde desees
        return redirect('v_productos')
    else:
        # Si el usuario no está autenticado, redirige a la página de inicio de sesión o muestra un mensaje de error
        return redirect('v_login')