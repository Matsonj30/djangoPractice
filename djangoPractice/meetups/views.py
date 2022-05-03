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
  try:
    selected_meetup = Meetup.objects.get(slug=meetup_slug) #entry where this condition is met
    return render(request, 'meetups/meetup-details.html', {
      'meetup_found' : True,
      'meetup_details':selected_meetup
  })
  except Exception as exc:
    return render(request, 'meetups/meetup-details.html',{
      'meetup_found' : False
    })