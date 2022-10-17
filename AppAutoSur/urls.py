from django.urls import path, include
from AppAutoSur.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    
    path("", inicio, name="inicio"),
    
    path("Fiat/", fiat, name="fiat"),
    path("Renault/", renault, name="renault"),
    path("Citroen/", citroen, name="citroen"),
    path("Peugeot/", peugeot, name="peugeot"),
    path("RenaultFormulario/", RenaultFormulario, name="RenaultFormulario"),
    path("CitroenFormulario/", CitroenFormulario, name="CitroenFormulario"),
    path("PeugeotFormulario/", PeugeotFormulario, name="PeugeotFormulario"),
    path("FiatFormulario/", FiatFormulario, name="FiatFormulario"),
    path("busquedaRenault/", busquedaRenault, name="busquedaRenault"),
    path("buscar/", buscar, name="buscar"),
    path("LeerRenault/", leerRenault, name="LeerRenault"),
    path("EditarRenault/<id>", editarRenault, name="EditarRenault"),
    path("EliminarRenault/<id>", eliminarRenault, name="EliminarRenault"),
    path("LeerCitroen/", leerCitroen, name="LeerCitroen"),
    path("EditarCitroen/<id>", editarCitroen, name="EditarCitroen"),
    path("EliminarCitroen/<id>", eliminarCitroen, name="EliminarCitroen"),
    path("LeerPeugeot/", leerPeugeot, name="LeerPeugeot"),
    path("EditarPeugeot/<id>", editarPeugeot, name="EditarPeugeot"),
    path("EliminarPeugeot/<id>", eliminarPeugeot, name="EliminarPeugeot"),
    path("LeerFiat/", leerFiat, name="LeerFiat"),
    path("EditarFiat/<id>", editarFiat, name="EditarFiat"),
    path("EliminarFiat/<id>", eliminarFiat, name="EliminarFiat"),
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name='AppAutoSur/logout.html'), name="logout"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("SinContenido/", sin_contenido, name="SinContenido"),
    path("AcercaDeNosotros/", acerca_de_nosotros, name="AcercaDeNosotros"),
    path("Chat/", include ("Chat.urls")),

]
