from django.contrib import admin
from eventfoldersrc.models import Venue
from eventfoldersrc.models import Catering
from eventfoldersrc.models import LightsAndSounds

# Register your models here.
admin.site.register(Venue)
admin.site.register(Catering)
admin.site.register(LightsAndSounds)