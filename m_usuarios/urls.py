from django.urls import path
from .views import (
    v_login,
    v_registro,
    cerrar_sesion,
    v_logiin
)
urlpatterns = [
    path('login/',v_login, name="v_login"),
    path('registro/',v_registro, name="v_registro"),
    path("cerrar_sesion/", cerrar_sesion, name="cerrar_sesion"),
    path('login/', v_logiin, name='logiin')
]