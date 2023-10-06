from django.shortcuts import render, redirect
from .formulario import (Formulario_login, Formulario_reg)
from sweetify import success,warning
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def v_login (request):
    form = Formulario_login(request.POST or None)
    if request.method == 'POST':
            usuario = request.POST['nombre_usuario']
            password = request.POST['contrasenia_usuario']
            usuario_valido = authenticate(request, username = usuario, password = password)
            if usuario_valido is not None:
                login(request, usuario_valido)
                success(request, f"Bienvenido {usuario_valido.username}")
                return(redirect('v_inicio'))
            if usuario_valido is None:
                warning( request, 'ups... :(', text='No se logro iniciar sesión, corrobore sus datos!', button='Continuar')
                return(redirect('logiin'))
    datos = {
        'formulario': form,
    }
    return render(request, 'login.html', datos)

def v_logiin (request):
    form = Formulario_login(request.POST or None)
    datos = {
        'formulario': form,
    }
    return render(request, 'login.html', datos)

def v_registro (request):
    if request.method == 'GET':
        datos={
            'formulario': Formulario_reg()
        }
        return render(request, 'registro.html', datos)
    if request.method == 'POST':
        datos_usuario = Formulario_reg(data = request.POST)
        es_valido = datos_usuario.is_valid()
        if es_valido:
            datos_usuario.save()
            success(request, 'Registro exitoso', text='Bienvenido!', timer= 3000, button='Continuar')
            return redirect ('v_login')
        datos = {
            'formulario': datos_usuario
        }
        warning( request, 'ups... :(', text='No se logro registrar, corrobore sus datos!', button='Continuar')
        return render(request, 'registro.html', datos)
    
def cerrar_sesion(request):
    if request.user.is_authenticated:
        logout(request)
        success(
            request,
            "Correcto",
            text="Tu sesion se cerro correctamente",
            button="OK",
            timer=3000,
        )
        return redirect("v_inicio")
    
