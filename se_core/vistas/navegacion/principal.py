# Vistas para la navegación general del aplicativo

from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'se_core/index.html')


def acercade(request):
    return render(request, 'se_core/acercade.html')


def misionvision(request):
    return render(request, 'se_core/misionvision.html')


def contactanos(request):
    return render(request, 'se_core/contactenos.html')


def iniciarsesion(request):
    return render(request, 'se_core/inicio_frm.html')


def loginn(request):
    correo = request.POST['correo']
    clave = request.POST['clave']

    if correo == "harolmgzapata@gmail.com" and clave == "1234":
        return HttpResponse(f"Usuario válido - Correo: {correo}, Clave: {clave}")
    else:
        mensaje = "* Datos no válidos..."
        contexto = {'mensaje': mensaje}
        return render(request, 'se_core/inicio_frm.html', contexto)