from django.shortcuts import render
from .models import Peugeot, Fiat, Renault, Citroen, Avatar
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate 
from django.contrib.auth.decorators import login_required

def inicio(request):
    avatar = None
    if request.user.is_authenticated:
        lista=Avatar.objects.filter(user=request.user)
        if len(lista)!=0:
            avatar=lista[0].imagen.url
    return render (request, "AppAutoSur/inicio.html", {"avatar":avatar})

def sin_contenido(request):
    return render (request, "AppAutoSur/SinContenido.html", {"avatar":obtenerAvatar(request)})


def acerca_de_nosotros(request):
    return render (request, "AppAutoSur/AcercaDeNosotros.html", {"avatar":obtenerAvatar(request)})

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
    return render (request, "AppAutoSur/fiat.html", {"avatar":obtenerAvatar(request)})

def renault(request):
    return render (request, "AppAutoSur/LeerRenault.html", {"avatar":obtenerAvatar(request)})

def citroen(request):
    return render (request, "AppAutoSur/LeerCitroen.html", {"avatar":obtenerAvatar(request)})

def peugeot(request):
    return render (request, "AppAutoSur/peugeot.html", {"avatar":obtenerAvatar(request)})



def busquedaRenault(request):
    return render(request, "AppAutoSur/busquedaRenault.html", {"avatar":obtenerAvatar(request)})

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
def FiatFormulario(request):
    
    if request.method=="POST":
        form= FiatForm(request.POST)
        if form.is_valid():
                info= form.cleaned_data
                renault= Fiat(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html", {"mensaje":"AGREGADO EXITOSAMETE", "avatar":obtenerAvatar(request)})
    else:
        form= FiatForm()
    return render(request, "AppAutoSur/FiatFormulario.html", {"form":form, "avatar":obtenerAvatar(request)})

def leerFiat(request):
    fiats=Fiat.objects.all()
    respuesta= {"fiats": fiats, "avatar":obtenerAvatar(request)}
    return render (request,  "AppAutoSur/LeerFiat.html", respuesta)

def eliminarFiat(request, id):
    fiat=Fiat.objects.get(id=id)
    fiat.delete()
    fiats=Fiat.objects.all()
    respuesta={"fiats":fiats, "avatar":obtenerAvatar(request)}
    return render (request, "AppAutoSur/LeerFiat.html", respuesta)

def editarFiat(request, id):
    fiat=Fiat.objects.get(id=id)
    if request.method=="POST":
        form=FiatForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            fiat.version=informacion['version']
            fiat.año=informacion['año']
            fiat.save()
            fiats=Fiat.objects.all()
            respuesta={"fiats":fiats,"avatar":obtenerAvatar(request)}
            return render (request, "AppAutoSur/LeerFiat.html", respuesta)

    else:
        form=FiatForm(initial={'version':fiat.version, 'año':fiat.año}) 
    return render(request, 'AppAutoSur/EditarFiat.html', {'form':form, 'fiat':fiat, "avatar":obtenerAvatar(request)})



@login_required
def PeugeotFormulario(request):
    
    if request.method=="POST":
        form= PeugeotForm(request.POST)
        if form.is_valid():
                info= form.cleaned_data
                renault= Peugeot(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html", {"mensaje":"AGREGADO EXITOSAMETE", "avatar":obtenerAvatar(request)})
    else:
        form= PeugeotForm()
    return render(request, "AppAutoSur/PeugeotFormulario.html", {"form":form, "avatar":obtenerAvatar(request)})

def leerPeugeot(request):
    peugeots=Peugeot.objects.all()
    respuesta= {"peugeots": peugeots, "avatar":obtenerAvatar(request)}
    return render (request,  "AppAutoSur/LeerPeugeot.html", respuesta)

def eliminarPeugeot(request, id):
    peugeot=Peugeot.objects.get(id=id)
    peugeot.delete()
    peugeots=Peugeot.objects.all()
    respuesta={"peugeots":peugeots, "avatar":obtenerAvatar(request)}
    return render (request, "AppAutoSur/LeerPeugeot.html", respuesta)

def editarPeugeot(request, id):
    peugeot=Peugeot.objects.get(id=id)
    if request.method=="POST":
        form=PeugeotForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            peugeot.version=informacion['version']
            peugeot.año=informacion['año']
            peugeot.save()
            peugeots=Peugeot.objects.all()
            respuesta={"peugeots":peugeots,"avatar":obtenerAvatar(request)}
            return render (request, "AppAutoSur/LeerPeugeot.html", respuesta)

    else:
        form=PeugeotForm(initial={'version':peugeot.version, 'año':peugeot.año}) 
    return render(request, 'AppAutoSur/EditarPeugeot.html', {'form':form, 'peugeot':peugeot, "avatar":obtenerAvatar(request)})


@login_required
def RenaultFormulario(request):
    
    if request.method=="POST":
        form= RenaultForm(request.POST)
        print(form)
        if form.is_valid:
                info= form.cleaned_data
                renault= Renault(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html", {"mensaje":"AGREGADO EXITOSAMETE", "avatar":obtenerAvatar(request)})
    else:
        form= RenaultForm()
    return render(request, "AppAutoSur/RenaultFormulario.html", {"form":form, "avatar":obtenerAvatar(request)})


def leerRenault(request):
    renaults=Renault.objects.all()
    respuesta= {"renaults": renaults, "avatar":obtenerAvatar(request)}
    return render (request,  "AppAutoSur/LeerRenault.html", respuesta)

def eliminarRenault(request, id):
    renault=Renault.objects.get(id=id)
    renault.delete()
    renaults=Renault.objects.all()
    respuesta={"renaults":renaults, "avatar":obtenerAvatar(request)}
    return render (request, "AppAutoSur/LeerRenault.html", respuesta)

def editarRenault(request, id):
    renault=Renault.objects.get(id=id)
    if request.method=="POST":
        form=RenaultForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            renault.version=informacion['version']
            renault.año=informacion['año']
            renault.save()
            renaults=Renault.objects.all()
            respuesta={"renaults":renaults,"avatar":obtenerAvatar(request)}
            return render (request, "AppAutoSur/LeerRenault.html", respuesta)

    else:
        form=RenaultForm(initial={'version':renault.version, 'año':renault.año}) 
    return render(request, 'AppAutoSur/EditarRenault.html', {'form':form, 'renault':renault, "avatar":obtenerAvatar(request)})

@login_required
def CitroenFormulario(request):
    
    if request.method=="POST":
        form= CitroenForm(request.POST)
        if form.is_valid():
                info= form.cleaned_data
                renault= Citroen(version=info["version"], año=info["año"])
                renault.save()
                return render (request, "AppAutoSur/inicio.html", {"mensaje":"AGREGADO EXITOSAMETE", "avatar":obtenerAvatar(request)})
    else:
        form= CitroenForm()
    return render(request, "AppAutoSur/CitroenFormulario.html", {"form":form, "avatar":obtenerAvatar(request)}) 


def leerCitroen(request):
    citroens=Citroen.objects.all()
    respuesta= {"citroens": citroens, "avatar":obtenerAvatar(request)}
    return render (request,  "AppAutoSur/LeerCitroen.html", respuesta)

def eliminarCitroen(request, id):
    citroen=Citroen.objects.get(id=id)
    citroen.delete()
    citroens=Citroen.objects.all()
    respuesta={"citroens":citroens, "avatar":obtenerAvatar(request)}
    return render (request, "AppAutoSur/LeerCitroen.html", respuesta)

def editarCitroen(request, id):
    citroen=Citroen.objects.get(id=id)
    if request.method=="POST":
        form=CitroenForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            citroen.version=informacion['version']
            citroen.año=informacion['año']
            citroen.save()
            citroens=Citroen.objects.all()
            respuesta={"citroens":citroens,"avatar":obtenerAvatar(request)}
            return render (request, "AppAutoSur/LeerCitroen.html", respuesta)

    else:
        form=CitroenForm(initial={'version':citroen.version, 'año':citroen.año}) 
    return render(request, 'AppAutoSur/EditarCitroen.html', {'form':form, 'citroen':citroen, "avatar":obtenerAvatar(request)})


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)

            if user is not None:
                login(request, user)
                return render (request, "AppAutoSur/inicio.html", {"mensaje":f"Bienvenido {usuario}", "avatar":obtenerAvatar(request)})

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


@login_required
def editarPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form=UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info['email']
            usuario.password1=info['password1']
            usuario.password2=info['password2']
            usuario.first_name=info['first_name']
            usuario.last_name=info['last_name']
            usuario.save()

            return render (request, "AppAutoSur/inicio.html", {'mensaje': "Perfil editado correctamente", "avatar":obtenerAvatar(request)})
    
    else:
        form=UserEditForm(instance=usuario)

    return render (request, "AppAutoSur/editarPerfil.html", {'form':form, 'usuario':usuario, "avatar":obtenerAvatar(request)})


@login_required
def agregarAvatar(request):
    if request.method=="POST":
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if (len(avatarViejo)>0):
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render (request, "AppAutoSur/inicio.html", {"usuario":request.user, "mensaje":'AVATAR AGREGADO EXISTOSAMENTE', "imagen":avatar.imagen.url})
        else:
            return render (request, "AppAutoSur/inicio.html", {"usuario":request.user, "mensaje":'FORMULARIO INVALIDO'})
    else:
        formulario=AvatarForm()
        return render (request, "AppAutoSur/agregarAvatar.html", {"formulario":formulario, "usuario":request.user})

def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/avatares/avatarpordefecto.png"
    return imagen