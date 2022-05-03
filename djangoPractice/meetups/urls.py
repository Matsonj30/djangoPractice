from django.urls import path
from . import views


urlpatterns = [ #has to be written exactly like this
    path('meetups/', views.index, name='all-meetups' ), #domain.com/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail') #dynamic url     #domain.com/meetups/<dynamic-meetup-title> etc.
    
] 