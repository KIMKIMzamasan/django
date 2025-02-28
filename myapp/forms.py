from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['firstname', 'middlename', 'lastname', 'username', 'password']
        
    password = forms.CharField(widget=forms.PasswordInput)
