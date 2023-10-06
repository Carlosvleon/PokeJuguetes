from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    PositiveIntegerField,
    DateTimeField,
    IntegerField,
    Sum,
    F,
)
from django.contrib.auth.models import  User
from m_productos.models import Producto


class Venta(Model):
    id_usuario = ForeignKey(User,on_delete=CASCADE)
    monto_total = IntegerField(default=0)
    fecha_compra = DateTimeField(auto_now_add=True)

    # retorna id
    def __str__ (self):
        return f"{self.id}"
    @property
    def total(self):
        return self.detalle_venta_set.aggregate(
            total=Sum(F("valor_producto") * F("cant_producto"), output_field=PositiveIntegerField())
        )["total"]
    
    class Meta:
        db_table = 'venta'
        verbose_name = 'pedido'
        verbose_name = 'pedidos'
        ordering = ['id']
        

class Detalle_Venta(Model):
    id_venta = ForeignKey(Venta, on_delete=CASCADE)
    id_producto = ForeignKey(Producto, on_delete=CASCADE)
    valor_producto = IntegerField(default=0)
    cant_producto = IntegerField(default=0)
    class Meta:
        db_table = 'detalle_venta'
        verbose_name = 'detalle_pedido'
        verbose_name = 'detalle_pedidos'
        ordering = ['id']

    def __str__ (self):
        return f"{self.id_producto.nom_producto} "