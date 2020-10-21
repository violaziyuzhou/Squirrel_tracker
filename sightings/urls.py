  
from django.urls import path

from . import views


urlpatterns = [
    path('', views.sightings, name='all_squirrels'),
    path('stats', views.stats, name = 'stats'),
    path('add/', views.add, name = 'add'),
    path('<str:squirrel_id>/', views.unique_squirrel_id, name='squirrel_id'),
]
