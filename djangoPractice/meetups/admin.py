from django.contrib import admin

from .models import Meetup,Location,Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin): #can control how meetups are presented
    list_display = ('title', 'date','location') #this will split the model into two columns
                                    #anything named in models.py can be placed here
    #filter many objects
    list_filter = ('location','date') #need comma so it is a tuple
    #have certain fields already filled out
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Meetup, MeetupAdmin) #this ensures the admin page will see this
admin.site.register(Location)
admin.site.register(Participant)