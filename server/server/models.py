from django.db import models
from django.contrib.auth.models import User
from time import time

# Create your models here.

class Pin(models.Model):
	fingerprint = models.TextField()
	name = models.CharField(max_length=100,blank=True)
	email = models.CharField(max_length=100, blank=True)
	number = models.CharField(max_length=20, blank=True)