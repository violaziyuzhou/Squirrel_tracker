from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    Longitude = models.FloatField(
            help_text=_('Longitude'),
            )
    
    Latitude = models.FloatField(
        help_text=_('Latitude'),
        )
    
    Unique_squirrel_id = models.CharField(
        max_length=100,
        help_text=_('Unique Squirrel ID'),
        unique = True,
        )
    
    Shift = models.CharField(
        max_length=100,
        help_text= _('Shift'),
        )
   
    Date = models.DateField(
            help_text=_('Date'),
            )

    Age = models.CharField(
            max_length=100,
            help_text=_('Age'),
            )

    Primary_Fur_Color = models.CharField(
            max_length = 100,
            help_text=_('Primary Fur Color'),
            )

    Location = models.CharField(
            max_length=100,
            help_text=_('Location'),
            )

    Specific_location=models.CharField(
            max_length=100,
            help_text=_('Specific Location'),
            )
    
    Running = models.BooleanField(
            null = True,
            blank = True
            )
    
    Chasing = models.BooleanField(
            null = True,
            blank = True
            )

    Climbing = models.BooleanField(
            null = True,
            blank = True
            )

    Eating = models.BooleanField(
            null = True,
            blank = True
            )

    Foraging = models.BooleanField(
            null = True,
            blank = True
            )

    Other_activities=models.CharField(
            max_length=100,
            help_text=_('Other Activities'),
            null = True)

    Kuks = models.BooleanField(
            null = True,
            blank = True
            )

    Quaas = models.BooleanField(
            null = True,
            blank = True
            )

    Moans = models.BooleanField(
            null = True,
            blank = True
            )

    Tail_flags = models.BooleanField(
            null = True,
            blank = True
            )

    Tail_twitche = models.BooleanField(
            null = True,
            blank = True
            )

    Approaches = models.BooleanField(
            null = True,
            blank = True
            )

    Indifferent = models.BooleanField(
            null = True,
            blank = True
            )

    Runs_from = models.BooleanField(
            null = True,
            blank = True
            )
