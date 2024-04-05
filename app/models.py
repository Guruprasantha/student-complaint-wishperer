from django.db import models

# Create your models here.
class Register(models.Model):
    id=models.AutoField(primary_key=True)
    uname=models.CharField(max_length=20)
    mobno=models.IntegerField(null=True)
    email=models.CharField(max_length=20)
    pwrd=models.CharField(max_length=20)

    def __str__(d):
        return d.uname

class pcm(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    mobno=models.IntegerField(null=True)
    comcat=models.CharField(max_length=50)
    comdt=models.DateTimeField()
    comdis=models.CharField(max_length=100)
    acta=models.CharField(max_length=50)
  
    

class adminl(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username
    
class Actiontake(models.Model):
    name=models.CharField(max_length=20)
    mobno=models.IntegerField(null=True)
    comcat=models.CharField(max_length=50)
    comdt=models.DateTimeField()
    comdis=models.CharField(max_length=100)
    acta=models.CharField(max_length=50)
    actionname=models.CharField(max_length=50)
    actiondis=models.CharField(max_length=500)
    actiondate=models.DateTimeField()

    def __str__(self):
        return self.name




