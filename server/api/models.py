from django.db import models
from django.contrib.auth.models import User
from time import time

# Create your models here.

class Pin(models.Model):
	fingerprint = models.TextField(unique=True)
	name = models.CharField(max_length=100,blank=True)
	email = models.CharField(max_length=100, blank=True)
	number = models.CharField(max_length=20, blank=True)

	def __unicode__(self):
		ret = str(self.id) + " " + self.name
		return ret

class Shake(models.Model):
	fingerprint = models.ForeignKey(Pin)
	lat = models.TextField()
	lon = models.TextField()
	timestamp = models.TextField()

	def __unicode__(self):
		return lat+lon