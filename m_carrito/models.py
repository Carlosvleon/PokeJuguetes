from django.db.models import (
    Model,
    ForeignKey,
    CASCADE,
    PositiveIntegerField
)
from m_productos.models import Producto
from  django.contrib.auth.models import User

# Create your models here.
class Carrito(Model):
    id_usuario = ForeignKey(User,on_delete=CASCADE)
    id_producto=ForeignKey(Producto, on_delete=CASCADE)
    cantidad=PositiveIntegerField()
    def __str__ (self):
        return str(self.id_usuario)
    def calcular_total(self):
        return self.cantidad * self.id_producto.valor_producto
    class Meta:
        db_table = "carrito"
        verbose_name = "carrito"
        verbose_name_plural = "carrito"
        ordering = ["id"]
