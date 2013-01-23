__author__ = 'User'

from  django import forms
from  sprofile.models import User as Profile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude=['user','email']