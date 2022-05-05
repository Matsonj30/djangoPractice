from django.urls import path
from . import views


urlpatterns = [ #has to be written exactly like this
    path('', views.index, name='all-meetups' ), #domain.com/meetups
    path('<slug:meetup_slug>/confirmation', views.confirmation, name='confirm-registration'), #put before dynamic segment
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), #dynamic url     #domain.com/meetups/<dynamic-meetup-title> etc.
    #this is where unique paths are made
    #can add meetups/  at the front if want
] 