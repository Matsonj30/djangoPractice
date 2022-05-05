from io import open_code
from re import T
from tkinter import CASCADE
from django.db import models

# Create your models here.

#one location can be used for many meetups
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})' #how the value should be viewed if requested 

class Participant(models.Model):
    email = models.EmailField(unique=True) #includes @ i guess

    def __str__(self):
        return self.email 

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True) #itll know which format to use with prepopualted_fields
    description = models.TextField() #for longer text
    image = models.ImageField(upload_to = 'images') #for images duh
    #connect two tables together FOREIGN key is for one to many
    location = models.ForeignKey(Location, on_delete=models.CASCADE) #cascade will just delete up
    #can filter by values in any class ^

    #many to many
    participants = models.ManyToManyField(Participant, blank=True, null=True) #it can be a blank field, then put null in its spot
    organizer_email = models.EmailField()
    date = models.DateField()



    def __str__(self): #change the name of the object in administation 
        return f'{self.title} - {self.slug}'