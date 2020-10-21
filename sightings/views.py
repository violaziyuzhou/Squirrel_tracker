from django.shortcuts import render
from .models import squirrel
from .forms import apprequestform
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum

def sightings(request):
    squirrels = Squirrels.objects.all()
    context = {'squirrels': squirrels}
	return render(request, 'sightings/squirrels.html', context)


def unique_squirrel_id(request,squiid):
    sightings = squirrel.objects.get(id=squiid)
    context = {'sightings': sightings}
    if request.method=='POST':
        form = squirrel(request.POST)
    elif request.method=='GET':
        form = squirrel(request.GET)
    else:
        return JsonResponse({},status=405)
    sightings.Latitude=form.latitude
    sightings.Longitude=form.longitude
    sightings.Unique_squirrel_id=form.id
    sightings.Shift=form.shift
    sightings.Date=form.date
    sightings.Age=form.age
    return render(request, 'sightings/squirrelid.html', context)

def add(request):
    get_post_request(request)
    sightings = squirrel()
    context = {'sightings': sightings}
    return render(request, 'sightings/add.html', context)

def stats(request):
    la_sum = squirrel.objects.filter('Latitude').aggregate(nums=Sum('count'))
    lo_sum = squirrel.objects.filter('Longitude').aggregate(nums=Sum('count'))
    id_sum=0
    for i in squirrel.objects.filter('Unique_squirrel_id'):
        id_sum+=1
    shift_am=0
    shift_pm=0
    for i in squirrel.objects.filter('Shift'):
        if i =='PM'
            shift_pm+=1
        else:
            shift_am+=1
    age_juvenile=0
    age_adult=0
    age_unknown=0
    for i in squirrel.objects.filter('Age'):
        if i=="Juvenile":
            age_juvenile+=1
        elif i=="Adult":
            age_adult+=1
        else:
            age_unknown+=1
    context = {'la_sum':la_sum,'lo_sum':lo_sum,'id_sum':id_sum,'shift_am':shift_am,'shift_pm':shift_pm,'age_juvenile':age_juvenile,'age_adult':age_adult,'age_unknown':age_unknown}
    return render(request, 'sightings/stats.html', context)

