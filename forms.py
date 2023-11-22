# myapp/forms.py
from django import forms
from .models import UserProfile

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email']
        widgets = {'password': forms.PasswordInput()}

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


