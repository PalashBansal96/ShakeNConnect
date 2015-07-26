from django.contrib import admin
from api.models import *

# Register your models here.

Models = [Pin, Shake, Handshake]

admin.site.register(Models)







