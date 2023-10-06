from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'img_producto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'nom_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'desc_producto': forms.TextInput(attrs={'class': 'form-control'}),
            'stock_producto': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor_producto': forms.NumberInput(attrs={'class': 'form-control'}),
            'id_tipo_1': forms.Select(attrs={'class': 'form-control'}),
            'id_tipo_2': forms.Select(attrs={'class': 'form-control'}),
        }