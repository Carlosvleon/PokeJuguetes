from django.urls import path
from .views import agregar_al_carrito, restar_producto, limpiar_carrito,ver_carrito

urlpatterns = [
    path('carrito/', ver_carrito, name='ver_carrito'),
    path('carrito/agregar/<int:producto_id>/', agregar_al_carrito, name='Add'),
    path('carrito/restar/<int:producto_id>/', restar_producto, name='Sub'),
    path('carrito/limpiar/', limpiar_carrito, name='CLS'),
]