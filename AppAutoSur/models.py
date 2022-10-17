from django.db import models
from django.contrib.auth.models import User

class Peugeot(models.Model):
    version=models.CharField(max_length=50)
    año=models.IntegerField()
    imagen=models.ImageField(upload_to='imagenes_peugeot',null=True)

    def __str__(self):
        return "Peugeot "+(self.version)+" "+str(self.año)


class Fiat(models.Model):
    version= models.CharField(max_length=50)
    año=models.IntegerField()
    imagen=models.ImageField(upload_to='imagenes_fiat', null=True)

    def __str__(self):
        return "Fiat " + self.version + " " + str(self.año)
        

class Renault(models.Model):
    version= models.CharField(max_length=50)
    año=models.IntegerField()
    imagen=models.ImageField(upload_to='imagenes_renault', null=True)

    def __str__(self):
        return "Renault "+(self.version)+" "+str(self.año)

class Citroen(models.Model):
    version= models.CharField(max_length=50)
    año=models.IntegerField()
    imagen=models.ImageField(upload_to='imagenes_citroen', null=True)

    def __str__(self):
        return "Citroen "+(self.version)+" "+str(self.año)

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True)