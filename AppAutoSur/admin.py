from django.contrib import admin

from AppAutoSur.models import Avatar, Citroen, Fiat, Renault
from Chat.models import Mensaje

admin.site.register(Citroen)
admin.site.register(Fiat)
admin.site.register(Renault)
admin.site.register(Avatar)
admin.site.register(Mensaje)
