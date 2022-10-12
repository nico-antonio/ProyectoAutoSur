from django.urls import path
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
    path("EliminarRenault/<id>", eliminarRenault, name="EliminarRenault"),
    path("EditarRenault/<id>", editarRenault, name="EditarRenault"),
    path("login/", login_request, name="login"),
    path("register/", register, name="register"),
    path("logout/", LogoutView.as_view(template_name='AppAutoSur/logout.html'), name="logout"),


]
