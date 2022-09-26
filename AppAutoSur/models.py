from django.db import models

class Peugeot(models.Model):
    version=models.CharField(max_length=50)
    año=models.IntegerField()

    def __str__(self):
        return "Peugeot" (self.version)+" "+str(self.año)


class Fiat(models.Model):
    version= models.CharField(max_length=50)
    año=models.IntegerField()

    def __str__(self):
        return "Fiat"(self.version)+" "+(self.año)
        

class Renault(models.Model):
    version= models.CharField(max_length=50)
    año=models.IntegerField()
    
    def __str__(self):
        return "Renault"(self.version)+" "+(self.año)

class Citroen(models.Model):
    version= models.CharField(max_length=50)
    año=models.IntegerField()

    def __str__(self):
        return "Citroen"(self.version)+" "+(self.año)
