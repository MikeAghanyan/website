from django import forms
from .models import Contacts

class Contactus(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'email', 'subject', 'message']