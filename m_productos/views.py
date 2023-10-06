from django.shortcuts import render,redirect
from .models import Producto
from django.core.paginator import Paginator
from m_comentario.models import Comentario
from m_carrito.models import Carrito
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .formulario import ProductoForm
from django.db.models import Count
from django.contrib.auth import logout


# Create your views here.

def v_productos(request):
    productos = Producto.objects.all()

    comentarios_por_producto = Comentario.objects.values('id_producto').annotate(cantidad_comentarios=Count('id_producto'))
    comentarios_dict = {c['id_producto']: c['cantidad_comentarios'] for c in comentarios_por_producto}

    for producto in productos:
        producto.cantidad_comentarios = comentarios_dict.get(producto.id, 0)

    paginator = Paginator(productos, 10)  # Mostrar 10 productos por página
    page_number = request.GET.get('page')
    productos_paginados = paginator.get_page(page_number)


    contexto = {
        'productos': productos_paginados,
    }
    return render(request, 'productos.html', contexto)

@staff_member_required
def cargar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('v_productos')
    else:
        form = ProductoForm()

    contexto = {
        'form': form
    }
    return render(request, 'cargar_producto.html', contexto)

@staff_member_required
def editar_productos(request):
    productos = Producto.objects.all()

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        producto = Producto.objects.get(id=product_id)

        producto.stock_producto = request.POST.get('stock_producto')
        producto.valor_producto = request.POST.get('valor_producto')
        producto.desc_producto = request.POST.get('desc_producto')

        if 'img_producto' in request.FILES:
            producto.img_producto = request.FILES['img_producto']

        producto.save()
        return redirect('editar_productos')

    contexto = {
        'productos': productos
    }
    return render(request, 'editar_productos.html', contexto)

@login_required(login_url='login')
def acceso_restringido(request):
    if not request.user.is_superuser:
        logout(request)
        return redirect('login')
    else:
        return redirect('v_productos')