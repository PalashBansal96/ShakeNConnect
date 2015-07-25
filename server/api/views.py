from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import constant_time_compare
import json, hmac, base64, hashlib
from api.models import *
import datetime

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
def shake(request):
	if request.method == 'GET':
		print request.GET['lat']
		print request.GET['lon']
		print request.GET['time']
		print request.GET['f']
		return HttpResponse('done')
	else:
		raise Http404



'''
@csrf_exempt
def shake(request):
	if request.method == 'GET':
		try:
			f = request.GET['f']
			fingerprint = Pin.objects.get(fingerprint=f)
			lat = request.GET['lat']
			lon = request.GET['lon']
			t = request.GET['timestamp']
			timestamp = datetime.datetime.fromtimestamp(t)
			shake = Shake(fingerprint=fingerprint,lat=lat,lon=lon,timestamp=timestamp)
			shake.save()
'''

