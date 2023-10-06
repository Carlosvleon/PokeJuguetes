"""
URL configuration for Poke_Juguetes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import v_inicio
from m_enviocorreo.views import enviar_correo 

urlpatterns = [
    path('', v_inicio, name='v_inicio'),
    path('inicio/',v_inicio, name="v_inicio"),
    path('producto/',include('m_productos.urls')),
    path('usuario/', include('m_usuarios.urls')),
    path('venta/', include('m_venta.urls')),
    path('comentario/', include('m_comentario.urls')),
    path('carrito/', include('m_carrito.urls')),
    path('enviar_correo/<int:venta_id>/', enviar_correo, name='enviar_correo'),
    path('admin/', admin.site.urls)
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)