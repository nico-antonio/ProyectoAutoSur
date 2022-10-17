from http.client import HTTPResponse
from django.shortcuts import render
from .models import *

# Create your views here.

def mensaje (request):
    mensajes=Mensaje.objects.filter(receptor=request.user)
    return render (request, "AppAutoSur/mensajes.html", {"mensajes":mensajes})