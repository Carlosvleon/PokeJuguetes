from django.db.models import (
    Model,
    CharField,
    TextField,
    ImageField,
    PositiveIntegerField,
    ForeignKey,
    CASCADE
)

# Create your models here.
class Tipo_Producto(Model):
    nombre_tipo = CharField(max_length=50 )
    def __str__(self):
        return self.nombre_tipo
    class Meta:
        db_table = "Tipo de productos"
        verbose_name = "tipo_p"
        verbose_name_plural = "tipo productos"
        ordering = ["id"]

class Producto(Model):
    nom_producto = CharField(max_length=50, null=False,  unique=True)
    desc_producto = TextField(max_length=500, null=False)
    stock_producto = PositiveIntegerField(null=False)
    valor_producto = PositiveIntegerField(null=False)
    id_tipo_1 = ForeignKey(Tipo_Producto,on_delete=CASCADE, related_name='id_tipo_1')
    id_tipo_2 = ForeignKey(Tipo_Producto,on_delete=CASCADE, related_name='id_tipo_2')
    img_producto = ImageField( upload_to="fotos_pkm")
    def __str__(self):
        return (f"{self.id} - {self.nom_producto}")
    class Meta:
        db_table = "Productos"
        verbose_name = "producto"
        verbose_name_plural = "Productos"
        ordering = ["id"]