from django.shortcuts import render
from django.http import Http404

from sightings.models import Squirrel

def map(request):
    sightings=squirrel.objects.all()[:,100]
    context={'sightings':sightings}
    return render(request,'map/map.html',context)
                                   
