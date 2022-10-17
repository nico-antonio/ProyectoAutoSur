from django.urls import path
from Chat.views import *

urlpatterns = [
    
    path("Chat/", mensaje, name="Chat"),

]