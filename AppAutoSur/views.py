from django.shortcuts import render
from .models import Peugeot, Fiat, Renault, Citroen
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required

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

def peugeot(request):
    return render (request, "AppAutoSur/peugeot.html")

@login_required
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
        
@login_required
def CitroenFormulario(request):
    
    if request.method=="POST":
        form= CitroenForm(request.POST)
        print(form)
        if form.is_valid:
                info= form.cleaned_data
                renault= Citroen(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html")
    else:
        form= CitroenForm()
    return render(request, "AppAutoSur/CitroenFormulario.html", {"form":form}) 

@login_required
def FiatFormulario(request):
    
    if request.method=="POST":
        form= FiatForm(request.POST)
        print(form)
        if form.is_valid:
                info= form.cleaned_data
                renault= Fiat(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html")
    else:
        form= FiatForm()
    return render(request, "AppAutoSur/FiatFormulario.html", {"form":form})


@login_required
def PeugeotFormulario(request):
    
    if request.method=="POST":
        form= PeugeotForm(request.POST)
        print(form)
        if form.is_valid:
                info= form.cleaned_data
                renault= Peugeot(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html")
    else:
        form= PeugeotForm()
    return render(request, "AppAutoSur/PeugeotFormulario.html", {"form":form})

def leerRenault(request):
    renaults=Renault.objects.all()
    respuesta= {"renaults": renaults}
    return render (request,  "AppAutoSur/LeerRenault.html", respuesta)

def eliminarRenault(request, id):
    renault=Renault.objects.get(id=id)
    renault.delete()
    renaults=Renault.objects.all()
    respuesta={"renaults":renaults}
    return render (request, "AppAutoSur/LeerRenault.html", respuesta)

def editarRenault(request, id):
    renault=Renault.objects.get(id=id)
    if request.method=="POST":
        form=RenaultForm(request.POST)
        if form.is_valid:
            informacion=form.cleaned_data
            renault.version=informacion['version']
            renault.año=informacion['año']
            renault.save()
            renaults=Renault.objects.all()
            respuesta={"renaults":renaults}
            return render (request, "AppAutoSur/LeerRenault.html", respuesta)

    else:
        miformulario=RenaultForm(initial={'version':renault.version, 'año':renault.año}) 
    return render(request, 'AppAutoSur/EditarRenault.html', {'miformulario':miformulario, 'renault':renault})


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render (request, "AppAutoSur/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

            else:
                return render (request, "AppAutoSur/login.html", {"mensaje": "Error: Datos incorrectos", 'form':form})
        else:
            return render (request, "AppAutoSur/login.html", {"mensaje": "Datos incorectos", 'form':form})

    form=AuthenticationForm()

    return render(request, "AppAutoSur/login.html", {'form':form})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render (request, "AppAutoSur/inicio.html", {"mensaje":f"Bienvenido {username}, Usuario creado correctamente"})

    else:
        form=UserCreationForm()

    return render(request, "AppAutoSur/register.html", {'form':form})





