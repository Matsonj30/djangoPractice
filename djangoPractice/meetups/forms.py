from django import forms

from .models import Participant


""" class RegistrationForms(forms.Form):
    email = forms.EmailField(label='Your email') #this will not have affect on any database, it is just there to collect data thru forms
 """

class RegistrationForms(forms.ModelForm): #initially used forms.ModelForm, ModelForm is good for save method
    #this has django infer forms
    class Meta: #will infer a form from this field in the model
        model = Participant 
        fields = ['email']