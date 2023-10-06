# from django.shortcuts import render, redirect
# from .models import Comentario
# from m_productos.views import Producto
# from .formulario import FormularioComentario
# from django.contrib.auth.decorators import login_required

# def v_comentario(request, producto_id):
#     producto = Producto.objects.filter(id=producto_id)
#     comentario = Comentario.objects.filter(id_producto_id=producto_id)
#     contexto = {
#         'producto': producto,
#         'comentario': comentario,
#         'formulario': FormularioComentario()
#     }
#     return render(request, 'comentario.html', contexto)

# @login_required
# def nuevo_comentario(request):
#     if request.method == 'GET':
#         contexto = {
#             'formulario': FormularioComentario()
#         }
#         return render(request, 'nuevo_comentario.html', contexto)
#     if request.method == 'POST':
#         dato_formulario = FormularioComentario(request.POST)
#         if dato_formulario.is_valid():
#             comentario_guardado = dato_formulario.save()
#             comentario_guardado.usuario = request.user
#             comentario_guardado.save()
#             return redirect('v_comentario', producto_id=comentario_guardado.id_producto_id)
        
#         contexto = {
#             'formulario': dato_formulario
#         }
#         return render(request, 'nuevo_comentario.html', contexto)
from django.shortcuts import render, redirect
from .models import Comentario
from m_productos.views import Producto
from .formulario import FormularioComentario
from django.contrib.auth.decorators import login_required
from django.db.models import Count


def v_comentario(request, producto_id):
    producto = Producto.objects.filter(id=producto_id).first()
    comentarios = Comentario.objects.filter(id_producto_id=producto_id)
    cantidad_comentarios = comentarios.count()
    contexto = {
        'producto': producto,
        'comentarios': comentarios,
        'formulario': FormularioComentario(initial={'id_producto': producto_id}),
        'cantidad_comentarios': cantidad_comentarios
    }
    print(contexto)
    return render(request, 'comentario.html', contexto)

@login_required
def nuevo_comentario(request):
    if request.method == 'POST':
        formulario = FormularioComentario(request.POST)
        if formulario.is_valid():
            comentario = formulario.save(commit=False)
            comentario.id_usuario = request.user
            comentario.save()
            return redirect('v_comentario', producto_id=comentario.id_producto_id)
    else:

        formulario = FormularioComentario(initial={'id_producto': request.GET.get('producto_id')})
    contexto = {
        'formulario': formulario
    }
    return render(request, 'nuevo_comentario.html', contexto)
