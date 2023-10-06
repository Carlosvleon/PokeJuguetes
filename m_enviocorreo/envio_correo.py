from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponse


def envio_correo(destinatario, asunto, mensaje):
    send_mail(asunto, mensaje,'notificacion_pokejuguetes@hotmail.com',[destinatario])
