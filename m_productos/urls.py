from django.urls import path
from .views import (
    v_productos,
    cargar_producto,
    editar_productos
)
urlpatterns = [
    path('',v_productos, name="v_productos"),
    path('cargar/', cargar_producto, name='cargar_producto'),
    path('editar/', editar_productos, name='editar_productos'),
]