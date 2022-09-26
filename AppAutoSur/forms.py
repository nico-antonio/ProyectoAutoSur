from socket import fromshare
from django import forms

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