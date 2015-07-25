from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import constant_time_compare
import json, hmac, base64, hashlib
from api.models import *
import datetime
import math
 
def distance_on_unit_sphere(lat1, long1, lat2, long2):
 
    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
         
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc * 637810000

def amb(request):
    if request.method == 'GET':
        f = request.GET['f']
        user = Pin(fingerprint = f)
        try:
        	user.save()
        	return HttpResponse(user.id)
        except:
        	user = Pin.objects.get(fingerprint = f)
        	return HttpResponse(user.id)

@csrf_exempt
def reg(request):
	if request.method == 'POST':
		print 'yes'
		print request.POST['name']
		print request.POST['email']
		print request.POST['number']
		return HttpResponse(request.POST['name'])
	else:
		return HttpResponse("post nigga")

@csrf_exempt
def shake(request):	# shake
	if request.method == 'GET':
		try:
			f = request.GET['f']
		except:
			raise Http404
					
		fingerprint = Pin.objects.get(fingerprint = f)

		lat = request.GET['lat']
		lon = request.GET['lon']
		t = request.GET['timestamp']

		timestamp = datetime.datetime.fromtimestamp(t)

		shake = Shake(fingerprint = fingerprint, lat = lat,
					  lon = lon, timestamp = timestamp)

		shake.save()

		return HttpResponse("k niga")

