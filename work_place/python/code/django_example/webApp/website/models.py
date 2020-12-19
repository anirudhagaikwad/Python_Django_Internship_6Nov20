from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name=models.CharField(max_length=15)
    gender=models.CharField(max_length=5)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    message=models.CharField(max_length=100)


class IntroImg(models.Model):
    intimg=models.ImageField(upload_to="myimg/intro")

class Servi(models.Model):
    imge=models.ImageField(upload_to="webimg/serimg")    
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)

class PortProd1(models.Model):
    hname=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)  
    imge=models.ImageField(upload_to="webimg/prod1")  

class PortProd2(models.Model):
    hname=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)  
    imge=models.ImageField(upload_to="webimg/prod2")


class PortProd3(models.Model):
    hname=models.CharField(max_length=50)
    pname=models.CharField(max_length=50)  
    imge=models.ImageField(upload_to="webimg/prod3")

