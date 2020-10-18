from django.shortcuts import render
from django.http import Http404

from .models import Squirrel

def map(request):
  squirrels = Squirrel.objects.all()[:100]
  return render(request, 'map/map.html', {"map" = squirrels})
                                   
