from django.urls import path, include
from .views import (
    v_historial,
    procesar_venta,
    v_boleta

)

urlpatterns = [
    path("",procesar_venta, name='procesar_venta'),
    path('historial/',v_historial, name="v_historial"),
    path('boleta/<int:venta_id>',v_boleta, name="v_boleta"),
    path('enviar_correo/', include('m_enviocorreo.urls')),

]