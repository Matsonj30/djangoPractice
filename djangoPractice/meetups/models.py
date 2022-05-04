from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField() #for longer text
    image = models.ImageField(upload_to = 'images') #for images duh

    def __str__(self): #change the name of the object in administation 
        return f'{self.title} - {self.slug}'