from django.urls import path
from AppAutoSur.views import *

urlpatterns = [
    
    path("", inicio, name="inicio"),
    
    path("Fiat/", fiat, name="fiat"),
    path("Renault/", renault, name="renault"),
    path("Citroen/", citroen, name="citroen"),
    path("RenaultFormulario/", RenaultFormulario, name="RenaultFormulario"),
    path("busquedaRenault/", busquedaRenault, name="busquedaRenault"),
    path("buscar/", buscar, name="buscar"),
    
]
