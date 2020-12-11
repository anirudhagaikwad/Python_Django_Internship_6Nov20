from django.db import models

# Create your models here.

class ContactInfo(models.Model):
    name=models.CharField(max_length=15)
    gender=models.CharField(max_length=5)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    message=models.CharField(max_length=100)
