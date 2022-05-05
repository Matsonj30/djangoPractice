from turtle import title
from django.shortcuts import render
from .models import Meetup #not sure why the . is needed
from .forms import RegistrationForms
# Create your views here.

def index(request):
    meetups= Meetup.objects.all() #data from database / objects is a static field
  

    return render(request, 'meetups/index.html', { #return rendered template
      'meetups':meetups  #this is what is being passed into the html to be manipualted with {}
    })

def meetup_details(request, meetup_slug): #meetup_slug needs to match the identifier in urls
  try:
      selected_meetup = Meetup.objects.get(slug=meetup_slug) #entry where this condition is met
      if request.method == 'GET': #if we have a get request? huh
        registration_form = RegistrationForms()
        return render(request, 'meetups/meetup-details.html', {
          'meetup_found' : True,
          'meetup_details':selected_meetup,
          'form':registration_form
          })
      else:
        registration_form = RegistrationForms(request.POST) #Any incoming request will have a post property whch will have any submitted data
        #this will be parsed, and will be mapped to the fields in the form
        if registration_form.is_valid(): #tests for a valid email then returns boolean
          participant= registration_form.save() #this will save to the database, will also return instance of saved model
          selected_meetup.partipants.add(participant) #add a new related record to Meetup
          ###IF form IS Valid, we want to redirect to confirmation page###

      return render(request, 'meetups/meetup-details.html', { #always return this template reguardless of POST or GET
          'meetup_found' : True,
          'meetup_details':selected_meetup,
          'form':registration_form
          })
  except Exception as exc:
    return render(request, 'meetups/meetup-details.html',{
      'meetup_found' : False
    })