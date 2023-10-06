from django.forms import (
    ModelForm
)
from .models import Venta, Detalle_Venta

class FormularioVenta(ModelForm):
    class Meta:
        model = Venta
        fields = ['monto_total']

class FormularioDetalleVenta(ModelForm):
    class Meta:
        model = Detalle_Venta
        fields = ['valor_producto','cant_producto']