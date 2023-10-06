from django.contrib import admin
from .models import Venta, Detalle_Venta

# Register your models here.
admin.site.register([Venta, Detalle_Venta])