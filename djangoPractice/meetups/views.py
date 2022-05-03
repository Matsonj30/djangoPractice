from turtle import title
from django.shortcuts import render
from .models import Meetup #not sure why the . is needed

# Create your views here.

def index(request):
    meetups= Meetup.objects.all() #data from database / objects is a static field


    return render(request, 'meetups/index.html', { #return rendered template
      'meetups':meetups  #this is what is being passed into the html to be manipualted with {}
    })

def meetup_details(request, meetup_slug): #meetup_slug needs to match the identifier in urls
  selected_meetup = {'title': 'A first Meetup', 
                    'description':'This is the first meetup!'}
  return render(request, 'meetups/meetup-details.html', {
    'meetup_details':selected_meetup
  })