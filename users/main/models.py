from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    