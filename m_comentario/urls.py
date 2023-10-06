from django.urls import path, include
from .views import (
    v_comentario, 
    nuevo_comentario
)

urlpatterns = [
    path('<int:producto_id>',v_comentario, name="v_comentario"),
    path('nuevo_comentario/', nuevo_comentario, name='nuevo_comentario'),

]

