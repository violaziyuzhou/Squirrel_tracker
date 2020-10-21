from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Avg, Max, Min, Count
from .models import Squirrel




def stats(request):
    total = Squirrel.objects.count()
    lattitude = Squirrels.aggregate(minimum=Min('Latitude'),maximum=Max('Latitude'))
    longitude = Squirrels.aggregate(minimum=Min('Longitude'),maximum=Max('Longitude'))
    age  = Squirrel.objects.values('age').annotate(c=Count('age'))
    shift = Squirrel.objects.values('shift').annotate(c=Count('shift'))

    context = {'total': total,
		'lattitude': lattitude,
		'longitude': longitude,
		'age': age,
		'shift': shift,
		}
    return render(request, 'sightings/stats.html', context)
