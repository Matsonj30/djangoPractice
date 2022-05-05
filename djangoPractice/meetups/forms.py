from django import forms

from .models import Participant

class RegistrationForms(forms.ModelForm):
    #this has django infer forms
    class Meta: #will infer a form from this field in the model
        model = Participant 
        fields = ['email']