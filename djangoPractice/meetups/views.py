from turtle import title
from django.shortcuts import render


# Create your views here.

def index(request):
    meetups= [
        {'title': 'A First Meetup', 
        'location': 'New York', 
        'slug': 'a-first-meetup'},

        {'title': 'A Second Meetup', 
        'location': 'Paris',
        'slug': 'a-second-meetup'},
    ]
    return render(request, 'meetups/index.html', { #return rendered template
      'show_meetups': True,
      'meetups':meetups  #this is what is being passed into the html to be manipualted with {}
    })

def meetup_details(request, meetup_slug): #meetup_slug needs to match the identifier in urls
  selected_meetup = {'title': 'A first Meetup', 
                    'description':'This is the first meetup!'}
  return render(request, 'meetups/meetup-details.html', {
    'meetup_details':selected_meetup
  })