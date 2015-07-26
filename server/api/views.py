from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from api.models import *
import math, urllib2, json, datetime
 
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

def getlocation(lat, lon):
    req = "http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true"%(lat,lon)
    xml = urllib2.urlopen(req)
    obj = json.loads(xml.read())
    obj = obj['results'][0]
    return obj['formatted_address'].encode('ascii')


def amb(request):
    if request.method == 'GET':
        try:
            f = request.GET['f']
            user = Pin(fingerprint = f)
            try:
            	user.save()
            	return HttpResponse(user.id)
            except:
            	user = Pin.objects.get(fingerprint = f)
            	return HttpResponse(user.id)
        except:
            raise Http404
    else:
        raise Http404

@csrf_exempt
def reg(request):
    if request.method == 'POST':
        user = Pin.objects.get(id=request.POST['id'])
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.number = request.POST['number']
        user.git = request.POST['git']
        user.linkedin = request.POST['link']
        user.facebook = request.POST['fb']
        user.save()
        return HttpResponse(user.fingerprint)
    else:
        return HttpResponse("post niga")

@csrf_exempt
def shake(request):	# shake
    if request.method == 'GET':
        f = request.GET['f']
        fingerprint = Pin.objects.get(fingerprint = f)
        if not fingerprint.name:
            raise Http404
        latt = request.GET['lat']
        lonn = request.GET['lon']
        t = request.GET['time']
        shake = Shake(fingerprint = fingerprint, lat = latt, lon = lonn, timestamp = int(t))
        shake.save()
        return HttpResponse("k niga")
    else:
        raise Http404

def is_duplicate(a, b):
    if a.user1 == b.user1 and a.user2 == b.user2:
        return 1

    if a.user1 == b.user2 and a.user2 == b.user1:
        return 1

    else:
        return 0


def findhandshakes(request):
    allshakes = Shake.objects.all()

    allpossible  = []

    for i in range(len(allshakes)):
        for j in range(len(allshakes)):
            if abs(int(allshakes[i].timestamp) - int(allshakes[j].timestamp)) < 5000:
                if abs(float(allshakes[i].lat) - float(allshakes[j].lat)) < 0.001 and abs(float(allshakes[i].lon) - float(allshakes[j].lon)) < 0.001:
                    if allshakes[i].fingerprint != allshakes[j].fingerprint:
                        newshake = Handshake(user1 = allshakes[i].fingerprint, user2 = allshakes[j].fingerprint, lon = allshakes[i].lon, lat = allshakes[i].lat, timestamp = allshakes[i].timestamp)
                        allpossible.append(newshake)

    allpossible.sort(key = lambda x: x.timestamp)

    i = 0

    while True:
        if i == len(allpossible) - 1:
            break

        while (i < len(allpossible) - 1) and (is_duplicate(allpossible[i], allpossible[i + 1])):
            allpossible.pop(i + 1)

    for i in allpossible:
        i.address = getlocation(i.lat, i.lon)
        i.save()


    for i in allshakes:
        i.delete()

    return HttpResponse('all done')


def req(request):
    if request.method == 'GET':
        id = request.GET['id']
        user = Pin.objects.get(id=id)

        lit = []
        count = 0

        handshakes = Handshake.objects.all()
        for i in handshakes:
            if i.user1 == user and i.u1check==0:
                t = datetime.datetime.fromtimestamp(int(i.timestamp.encode('ascii'))/1000.0)
                count+=1
                lit.append(str(i.user2.id)[:25])
                lit.append(str(i.user2.name)[:25])
                lit.append(str(t)[:20])
                lit.append(str(i.address)[:58])
            if i.user2 == user and i.u2check==0:
                count+=1
                lit.append(str(i.user1.id)[:25])
                lit.append(str(i.user1.name)[:25])
                lit.append(str(i.t)[:20])
                lit.append(str(i.address)[:58])

        lit = [str(count)] + lit
        lit = '|'.join(lit)
        print lit
        return HttpResponse(lit)
    else:
        raise Http404

def fin(request):
	if request.method == 'GET':
		me = request.GET['me']
		you = request.GET['you']
		check = request.GET['s']

		handshakes = Handshake.objects.all()

		for i in handshakes:
			if i.user1.id == int(me) and i.user2.id == int(you) and i.u1check==0:
				if int(check)==1:
					i.u1check=1
					i.save()
					info = i.user2.name + "|" + i.user2.email + "|" + i.user2.number + "|" + i.user2.git + "|" + i.user2.linkedin + "|" + i.user2.facebook
				else:
					i.u1check=-1
					i.save()
					info = ''
				break
			if i.user2.id == int(me) and i.user1.id == int(you) and i.u2check==0:
				if int(check)==1:
					i.u2check=1
					i.save()
					info = i.user1.name + "|" + i.user1.email + "|" + i.user1.number + "|" + i.user1.git + "|" + i.user1.linkedin + "|" + i.user1.facebook
				else:
					i.u2check=-1
					i.save()
					info = ''
				break

		return HttpResponse(info)

	else:
		raise Http404