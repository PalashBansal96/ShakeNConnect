from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.utils.crypto import constant_time_compare
import json, hmac, base64, hashlib
from server.models import Pin

def amb(request):
    return HttpResponse('1')

'''
def amb(request):
    if request.method=='GET':
        f = request.GET['f']
        user = Pin(fingerprint=f)
        #user.save()
        return HttpResponse(user.id)
        '''