from django.shortcuts import render, redirect
from m_venta.models import Venta, Detalle_Venta
from django.contrib.auth.decorators import login_required
from sweetify import success
from .envio_correo import envio_correo

@login_required(login_url='/usuario/login')
def enviar_correo(request):
    if request.method == 'POST':
        venta = Venta.objects.latest('id')
        detalle_venta = Detalle_Venta.objects.filter(id_venta=venta)
        
        correo = request.user.email
        asunto = 'Comprobante de venta'
        cuerpo_correo = f"Detalles de la venta:\n\n"
        cuerpo_correo += f"ID de venta: {venta.id}\n"
        cuerpo_correo += "-----------------------------\n"
        cuerpo_correo += "Detalle de productos:\n"
        cuerpo_correo += "-----------------------------\n\n"
        for detalle in detalle_venta:
            cuerpo_correo += f"Producto: {detalle.id_producto}\n"
            cuerpo_correo += f"Cantidad: {detalle.cant_producto}\n"
            cuerpo_correo += f"Precio unitario: {detalle.valor_producto}\n\n"
        cuerpo_correo += "-----------------------------\n\n"
        cuerpo_correo += f"Total: {venta.total}\n\n"
        cuerpo_correo += "-----------------------------\n\n"
        cuerpo_correo += "Saludos! PokeJuguetes."

        envio_correo(correo, asunto, cuerpo_correo)
        print(venta)
        success(request, 'Correo enviado', text='boleta enviada a su correo', timer= 3000, button='Continuar')

    return redirect('v_boleta', venta )