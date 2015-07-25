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
	timestamp = models.BigIntegerField()

	def __unicode__(self):
		return self.lat + " " + self.lon

class Handshake(models.Model):
	user1 = models.ForeignKey(Pin, related_name = 'one')
	user2 = models.ForeignKey(Pin, related_name = 'two')
	lat = models.TextField()
	lon = models.TextField()	
	address = models.TextField()
	timestamp = models.TextField()
	u1check = models.IntegerField(default=0)
	u2check = models.IntegerField(default=0)

	def __unicode__(self):
		return self.user1.name + " " + self.user2.name