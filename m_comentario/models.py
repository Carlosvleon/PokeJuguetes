from django.db.models import (
    Model,
    CharField,
    TextField,
    ForeignKey,
    CASCADE,
    DateTimeField
)
from django.contrib.auth.models import  User
from m_productos.models import Producto

# Create your models here.

class Comentario(Model):
    id_producto = ForeignKey(Producto, on_delete=CASCADE)
    id_usuario = ForeignKey(User,on_delete=CASCADE)
    titulo_comentario = CharField(max_length=50,null=False)
    contenido_comentario = TextField(max_length=500, null=False)
    fecha_comentario = DateTimeField(auto_now_add=True)
    def __str__ (self):
        return str(self.id_producto)
    class Meta:
        db_table = "comentarios"
        verbose_name = "coment"
        verbose_name_plural = "comentarios"
        ordering = ["id"]


