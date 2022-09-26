from django.shortcuts import render
from .models import Peugeot, Fiat, Renault, Citroen
from django.http import HttpResponse
from .forms import *

def inicio(request):
    return render (request, "AppAutoSur/inicio.html")

#def peugeot(request):

    if request.method=="POST":    
        version = request.POST.get("version")
        año = request.POST.get("año")
        peugeot = Peugeot (version=version, año=año)
        peugeot.save()
        peugeot=Peugeot(version="Peugeot de prueba", año=2010)
        peugeot.save()
        texto=f"Peugeot creado"
        return HttpResponse(texto)

def fiat(request):
    return render (request, "AppAutoSur/fiat.html")

def renault(request):
    return render (request, "AppAutoSur/renault.html")

def citroen(request):
    return render (request, "AppAutoSur/citroen.html")


def RenaultFormulario(request):
    
    if request.method=="POST":
        form= RenaultForm(request.POST)
        print(form)
        if form.is_valid:
                info= form.cleaned_data
                renault= Renault(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html")
    else:
        form= RenaultForm()
    return render(request, "AppAutoSur/RenaultFormulario.html", {"form":form})


def busquedaRenault(request):
    return render(request, "AppAutoSur/busquedaRenault.html")

def buscar(request):
    if request.GET['version']:
        version=request.GET['version']
        renaults=Renault.objects.filter(version__icontains=version)
        return render(request, "AppAutoSur/resultadosBusqueda.html", {"renault":renaults, "version":version})
    
    else:
        respuesta= "No enviaste datos"
   # respuesta=f"Estoy buscando autos Renault modelo: {request.GET['version']}"
    return HttpResponse(respuesta)
        