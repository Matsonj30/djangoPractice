from turtle import title
from django.forms import EmailField
from django.shortcuts import render, redirect
from .models import Meetup, Participant #not sure why the . is needed
from .forms import RegistrationForms
# Create your views here.

def index(request):
    meetups= Meetup.objects.all() #data from database / objects is a static field
  

    return render(request, 'meetups/index.html', { #return rendered template
      'meetups':meetups  #this is what is being passed into the html to be manipualted with {}
    })



def meetup_details(request, meetup_slug): #meetup_slug needs to match the identifier in urls
  try:
      #where slug = meetup_slug get the value
      selected_meetup = Meetup.objects.get(slug=meetup_slug) #entry where this condition is met
      if request.method == 'GET': #if we have a get request? huh
        registration_form = RegistrationForms()
      
      else:
        registration_form = RegistrationForms(request.POST) #Any incoming request will have a post property whch will have any submitted data
        #if a form is not valid, if we redirect to the same page, this form will store any error data :)
        
        #this will be parsed, and will be mapped to the fields in the form
        if registration_form.is_valid(): #tests for a valid email then returns boolean
          #user_email = registration_form.cleaned_data['email'] #will take the email key and will give us access to the user_email    
          #participant, _ = Participant.objects.get_or_create(email=user_email) #allows to us to either create or get an email if it already exists, returns tuple
          registration_form.save() #this will save to the database, will also return instance of saved model. this is not needed if using the LINE ABOVE ***
        
          #selected_meetup.partipants.add(participant) #add a new related record to Meetup THIS FIELD BREAKS everything somehow if using .save
          ###IF form IS Valid, we want to redirect to confirmation page###

          return redirect('confirm-registration', meetup_slug=meetup_slug) #redirect to a different url which is named in urls.py
          #this meetup slug needs to be defiend dynamically in urls.py^^
      return render(request, 'meetups/meetup-details.html', { #always return this template reguardless of POST or GET
          'meetup_found' : True,
          'meetup_details':selected_meetup,
          'form':registration_form
          })
          
  except Exception as exc:
    return render(request, 'meetups/meetup-details.html',{ #as named in file explorer
      'meetup_found' : False
    })


def confirmation(request, meetup_slug): #parameter name has to match name in URL.py
  meetup = Meetup.objects.get(slug=meetup_slug)
  return render(request, 'meetups/confirmation.html', {
    'meetup_details': meetup,
  })

