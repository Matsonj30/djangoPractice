from django.contrib import admin

from .models import Meetup
# Register your models here.

class MeetupAdmin(admin.ModelAdmin): #can control how meetups are presented
    list_display = ('title')


admin.site.register(Meetup) #this ensures the admin page will see this