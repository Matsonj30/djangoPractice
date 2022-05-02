from django.urls import path
from . import views

urlpatterns = [ #has to be written exactly like this
    path('meetups/', views.index ) #domain.com/meetups
] 