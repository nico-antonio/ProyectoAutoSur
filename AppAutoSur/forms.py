from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeugeotForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()
    imagen=forms.ImageField(label="Imagen", required=False)
   
class FiatForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()
    imagen=forms.ImageField(label="Imagen", required=False)

class RenaultForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()
    imagen=forms.ImageField(label="Imagen", required=False)

class CitroenForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()
    imagen=forms.ImageField(label="Imagen", required=False)

class UserCreationForm(UserCreationForm):
    email=forms.EmailField
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email=forms.EmailField(label="Modificar e-mail: ")
    password1=forms.CharField(label="Modificar contraseña: ", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la nueva contraseña: ", widget=forms.PasswordInput)
    last_name=forms.CharField()
    first_name=forms.CharField()

    class Meta:
        model=User
        fields=["email", "password1", "password2", "last_name", "first_name"]
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")