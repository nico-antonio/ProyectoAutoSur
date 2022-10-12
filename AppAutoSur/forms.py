from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeugeotForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()
   
class FiatForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()

class RenaultForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()

class CitroenForm(forms.Form):
    version = forms.CharField(max_length=50)
    año = forms.IntegerField()

class UserCreationForm(UserCreationForm):
    email=forms.EmailField
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}

