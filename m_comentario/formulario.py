
from django.forms import (
    ModelForm,
    Textarea,
    TextInput,
    HiddenInput
)
from .models import Comentario

class FormularioComentario(ModelForm):
    class Meta:
        model = Comentario
        fields = ['id_producto','titulo_comentario', 'contenido_comentario']
        widgets = {
            'titulo_comentario': TextInput(attrs={'class': 'form-control'}),
            'contenido_comentario': Textarea(attrs={'class': 'form-control'}),
            'id_producto': HiddenInput()
        }