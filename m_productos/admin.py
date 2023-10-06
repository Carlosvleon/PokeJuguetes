from django.contrib import admin
from .models import Tipo_Producto, Producto

# Register your models here.
admin.site.register([Tipo_Producto, Producto])