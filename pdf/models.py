from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100 , null=True)
    phone = models.CharField(max_length=100 , null=True)
    email = models.CharField(max_length=100 , null=True)
    school = models.CharField(max_length=100 , null=True)
    degree = models.CharField(max_length=100 , null=True)
    university = models.CharField(max_length=100 , null=True)
    skills = models.TextField(max_length=1000 , null=True)
    summary = models.TextField(max_length=1000 , null=True)
    workexperince = models.TextField(max_length=1000 , null=True)
    