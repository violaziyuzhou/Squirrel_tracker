from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect

from .forms import SquirrelForm

def add(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST, instance = squirrel)
        if form.isvalid():
            form.save()
            return redirect('/sightings/')
        else:
            form = SquirrelForm(instance = squirrel)
            context = {'form':form,}
        return render(request,'sightings/add.html',context)

