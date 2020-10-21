from django.shortcuts import render

def sightings(request):
    squirrels = Squirrels.objects.all()
    context = {'squirrels': squirrels}
	return render(request, 'sightings/squirrels.html', context)
